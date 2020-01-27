#!/usr/bin/env python
# aws disector
import requests
import json


ip_ranges = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json').json()['prefixes']


def get_all_ipv4():
    print('AWS Prefixes:')
    all_ipv4_json = json.dumps(ip_ranges, indent=4)
    print(all_ipv4_json)

def get_regions():
    print('AWS Regions:')
    region_list = [item['region'] for item in ip_ranges]
    regions = set(region_list)
    for region in regions:
        print(region)


def get_services():
    print('AWS Services:')
    service_list = [item['service'] for item in ip_ranges]
    services = set(service_list)
    for service in services:
        print(service)
    

def get_region_ipv4(region, service=None):
    assert type(region) is str, 'Parameter <region> must be a string.'
    assert type(service) is str or service is None, 'Optional parameter <service> must be a string.'  
    try:
        region = region.upper()
        if service is None:
            print(f'{region} IPv4 prefixes:')
            region_ipv4 = [item['ip_prefix'] for item in ip_ranges if item['region'].upper() == region]
        elif service is not None:
            service = service.upper()
            print(f'{region} IPv4 prefixes for {service} service:')
            region_ipv4 = [item['ip_prefix'] for item in ip_ranges if item['region'].upper() == region and item['service'].upper() == service]
        else:
            print('Something went wrong!')
        for ip in region_ipv4:
            print(ip)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except AssertionError as e:
        print(e)


def main():
    #get_all_ipv4()
    get_region_ipv4('us-gov-west-1')
    get_region_ipv4('us-gov-west-1', 'S3')
    #get_region_ipv4('us-gov-west-1', 'EC2')
    #get_regions()
    #get_services()

if __name__ == '__main__':
    main()
    
  #####################################################################################
  
  #!/usr/bin/env python
  # aws route_tracker

import requests
import json
from datetime import datetime

ip_ranges = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json').json()['prefixes']

def get_all_ipv4():
    all_ipv4_json = json.dumps(ip_ranges, indent=4)
    print(all_ipv4_json)

def get_regions():
    region_list = [item['region'] for item in ip_ranges]
    regions = set(region_list)
    for region in regions:
        print(region)

def get_services():
    service_list = [item['service'] for item in ip_ranges]
    services = set(service_list)
    for service in services:
        print(service)
    
def get_region_ipv4(region, service=None):
    """
    Return dictionary object with all IPv4 routes for a given AWS region and
    for a given AWS service if the service is provided.

    Parameters:
        region (str): The AWS region
        service (str, optional): AWS service in specified region

    Return:
        dict_object: 
            key: (str): region or regionservice
            value: (lst): list of IPv4 prefixes
    """
    try:
        assert type(region) is str, 'Parameter <region> must be a string.'
        assert type(service) is str or service is None, 'Optional parameter <service> must be a string.'  
        if service is None:
            region = region.lower()
            region_ipv4 = [item['ip_prefix'] for item in ip_ranges if item['region'] == region]
            dict_object = {region: region_ipv4}
        elif service is not None:
            region = region.lower()
            service = service.upper()
            region_ipv4 = [item['ip_prefix'] for item in ip_ranges if item['region'] == region and item['service'] == service]
            dict_object = {region + '_' + service: region_ipv4}
        return dict_object
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except AssertionError as e:
        print(e)

def save_region_ipv4(region, service=None):
    """
    Calls get_region_ipv4 function, and stores this information as a JSON file
    in the specified directory.

    Parameters:
        region (str): The AWS region
        service (str, optional): AWS service in specified region
    """
    try:
        assert type(region) is str, 'Parameter <region> must be a string.'
        assert type(service) is str or service is None, 'Optional parameter <service> must be a string.'  
        now = datetime.now()
        time_stamp = f'{now.year}-{now.month}-{now.day}-{now.hour}-{now.minute}-{now.second}'
        data = get_region_ipv4(region, service)
        the_json = json.dumps(data)
        directory = 'H:\\Cloud\\automation\\'
        if service is None:
            file_name = f'{region}_{time_stamp}.json'
        elif service is not None:
            file_name = f'{region}_{service}_{time_stamp}.json'
        else:
            print('Something went wrong!')
        with open(directory + file_name, 'w+') as fh:
            fh.write(the_json)
            print(f'File {file_name} saved at {directory}')
            print(the_json)
    except IOError as e:
        print(e)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except AssertionError as e:
        print(e)

def compare_region_ipv4(region, file_name, service=None):
    """
    Calls get_region_ipv4 function for the latest regional IPv4 information and
    retrives regional IPv4 information previously stored. Compare the latest with
    the stored IPv4 information and indicates if a change between the two is 
    detected. List both latest and stored information.

    Parameters:
        region (str): The AWS region
        file_name (str): Path and file name where information is stored
        service (str, optional): AWS service in specified region
    """   
    try:
        assert type(region) is str, 'Parameter <region> must be a string.'
        assert type(file_name) is str, 'Parameter <file_name> must be a string.'        
        assert type(service) is str or service is None, 'Optional parameter <service> must be a string.'         
        current_routes = get_region_ipv4(region, service)
        with open(file_name) as fh:
            stored_routes = json.load(fh)
        if current_routes == stored_routes:
            print(f'No change detected for region {region} & service {service}')
        elif current_routes != stored_routes:
            print(f'Change detected for region {region} & service {service}!')
        else:
            print('Something went wrong with elif clause')
        print('Current routes:', current_routes)
        print('Stored routes :', stored_routes)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except AssertionError as e:
        print(e)

def main():
    #get_all_ipv4()
    #get_regions()
    #get_services()
    #print(get_region_ipv4('us-gov-west-1'))
    #print(get_region_ipv4('us-gov-west-1', 'S3'))
    #save_region_ipv4('us-gov-west-1', 'EC2')
    #save_region_ipv4('us-gov-west-1', 'S3')
    compare_region_ipv4('us-gov-west-1', 'H:\Cloud\\automation\\us-gov-west-1_S3_2019-12-16-11-38-47.json', 'S3')
    compare_region_ipv4('us-gov-west-1', 'H:\Cloud\\automation\\us-gov-west-1_EC2_2019-12-16-11-2-58.json', 'EC2')

if __name__ == '__main__':
    main()
    
    #####################################################################################
    
# azure_gov_dissector
import json
import requests

uri = 'https://download.microsoft.com/download/6/4/D/64DB03BF-895B-4173-A8B1-BA4AD5D4DF22/ServiceTags_AzureGovernment_20200121.json'

ip_ranges = requests.get(uri).json()['values']


def get_all():
    Print('All values:')
    all = json.dumps(ip_ranges, indent=4)
    print(all)


def get_regions():
    print('Regions:')
    region_list = [item['properties']['region'] for item in ip_ranges]
    region_set = set(region_list)
    for region in region_set:
        print(region)


def get_ids():
    print('IDs:')
    id_list = [item['id'] for item in ip_ranges]
    id_set = set(id_list)
    for id in id_set:
        print(id)


def get_services():
    print('Services:')
    service_list = [item['properties']['systemService'] for item in ip_ranges]
    service_set = set(service_list)
    for service in service_set:
        print(service)


def get_region_ipv4(region, service=None):
    assert type(region) is str, 'Parameter <region> must be a string.'
    assert type(service) is str or service is None, 'Optional parameter <service> must be a string.'  
    try:
        region = region.lower()
        if service is None:
            print(f'{region} IPv4 prefixes:')
            region_ipv4_list = [item['properties']['addressPrefixes'] for item in ip_ranges if item['properties']['region'].lower() == region]
            flat_list = []
            for i in region_ipv4_list:
                flat_list.extend(i)
            list_set = set(flat_list)
            for prefix in list_set: 
                print(prefix)
        if service is not None:
            print(f'{region} IPv4 prefixes for {service} service:')
            service = service.lower()
            region_ipv4_list = [item['properties']['addressPrefixes'] for item in ip_ranges \
                 if item['properties']['region'].lower() == region and item['properties']['systemService'].lower() == service]
            for i in region_ipv4_list:
                for prefix in i:
                    print(prefix)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except AssertionError as e:
        print(e)


def main():
    #get_all()
    #get_regions()
    #get_services()
    get_region_ipv4('usgovvirginia')
    get_region_ipv4('usgovvirginia', 'AzureStorage')
    #get_ids()

if __name__ == '__main__':
    main()
    
   
      #####################################################################################
      
 #!/usr/bin/python3
"""This modules provides JSON encoded network information for O365.

The purpose of this module is to provide network information for Office 365 in
particular IPv4 and IPv6 route information for each service areas.

This modules parses the source JSON with filter functions. Each filter function
provides interesting data from a pre-defined set rules.

Web page:
https://docs.microsoft.com/en-us/office365/enterprise/office-365-u-s-government-gcc-high-endpoints

The source JSON is:
    https://endpoints.office.com/endpoints/USGovGCCHigh/?ClientRequestId=uuid

Module functions and information they provide:
    get_service_areas()
        Available service areas and display names

    get_all_items()
        Raw and complete source JSON

    get_er_exceptions()
        Express Route exceptions

    get_items_with_ips()
        All items from source JSON containing IPs

    get_common_ipv4()
        IPv4 networks for Microsoft 365 Common and Office Online

    get_common_ipv6()
        IPv6 networks for Microsoft 365 Common and Office Online

    get_exchange_ipv4()
        IPv4 networks for Exchange Online

    get_exchange_ipv6()
        IPv6 networks for Exchange Online

    get_sharepoint_ipv4()
        IPv4 networks for SharePoint Online and OneDrive for Business

    get_sharepoint_ipv6()
        IPv6 networks for SharePoint Online and OneDrive for Business

    get_skype_ipv4()
        IPv4 networks for Skype for Business Online and Microsoft Teams

    get_skype_ipv6()
        IPv6 networks for Skype for Business Online and Microsoft Teams

Example:
    from azure_endpoints import o365
    print(o365.get_service_areas())

Todo: Remove print statement from each

"""

import json
import requests
import ipaddress
import uuid

# Declare URL for source JSON and generate a random uuid for a complete URI
url = 'https://endpoints.office.com/endpoints/USGOVGCCHigh/?clientrequestid='
guid = str(uuid.uuid4())
uri = url+guid


def get_json(payload):
    """Select items with IP information and in the Common service area and fill
    set.

    Usage:
        get_common_ipv4()

    :return: JSON with Microsoft 365 Common and Office Online service IPv4 routes
    """
    try:
        the_json = json.dumps(payload, indent=4, sort_keys=True)
        return the_json
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


def get_data():
    """json_data is raw data; a list with all dict items.

    Usage:
        get_data():

    :return: JSON with O365 network information
    """
    try:
        response = requests.get(uri)
        json_data = response.json()
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    return json_data


def get_service_areas():
    """Declare the known service areas in a set and creates sets for service
    areas and service areas display names containers.

    Usage:
        get_service_areas()

    :return: JSON with service areas and service areas display names
    """
    known_service_areas = {'Exchange', 'Skype', 'SharePoint', 'Common'}
    service_areas_display = set()
    service_areas = set()
    try:
        for i in get_data():
            service_areas_display.add(i['serviceAreaDisplayName'])
            service_areas.add(i['serviceArea'])
        if known_service_areas != service_areas:
            print('Warning; known service areas does not mach available service areas!')
        service_areas_display_lst = list(service_areas_display)
        service_areas_display_dic = {'serviceAreaDisplayNames': service_areas_display_lst}
        service_areas_lst = list(service_areas)
        service_areas_dic = {'serviceAreas': service_areas_lst}
        all_service_areas_lst = [service_areas_dic, service_areas_display_dic]
        main_dic = {'serviceAreaInfo': all_service_areas_lst}
        return get_json(main_dic)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


def get_er_exceptions():
    """Provides items with Express Route exceptions
    Usage:
        get_er_exceptions()

    :return: JSON for items with ExpressRoute exceptions
    """
    express_route_exceptions_lst = []
    try:
        for i in get_data():
            if i['expressRoute'] is False:
                express_route_exceptions_lst.append(i)
        express_route_exceptions_dic = {'expressRoutesExceptions': express_route_exceptions_lst}
        return get_json(express_route_exceptions_dic)
    except ValueError as e:
        print(e)


def get_all_items():
    """Raw JSON for a given URI

    Usage:
        get_all_items()

    :return: Raw JSON from given IRI
    """
    try:
        return get_json(get_data())
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


def get_items_with_ips():
    """Select items with IP prefixes and create a formatted JSON file

    Usage:
        get_items_with_ips()

    :return: JSON with all items with IPs
    """
    all_items_with_ips_lst = []
    try:
        for i in get_data():
            if 'ips' in i:
                all_items_with_ips_lst.append(i)
        all_items_with_ips_dic = {'allItemsWithIPs': all_items_with_ips_lst}
        return get_json(all_items_with_ips_dic)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


def get_common_ipv4():
    """Select items with IP information and in the Common service area and fill
    set.

    Usage:
        get_common_ipv4()

    :return: JSON with Microsoft 365 Common and Office Online service IPv4 routes
    """
    common_ips_set = set()  # Set to eliminate duplicates
    try:
        for i in get_data():
            if 'ips' in i and i['serviceArea'] == 'Common' and i["expressRoute"] == True:
                common_ips = i['ips']
                for j in common_ips:
                    if type(ipaddress.ip_network(j)) is ipaddress.IPv4Network:
                        common_ips_set.add(j)
        common_ips_lst = list(common_ips_set)
        common_ips_dic = {'microsoft365CommonAndOfficeOnlineIPv4': common_ips_lst}
        return get_json(common_ips_dic)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


def get_common_ipv6():
    """Select items with IP information and in the Common service area and fill
     set.

    Usage:
        get_common_ipv6()

    :return: JSON with Microsoft 365 Common and Office Online service IPv6 routes
    """
    common_ips_set = set()  # Set to eliminate duplicates
    try:
        for i in get_data():
            if 'ips' in i and i['serviceArea'] == 'Common' and i["expressRoute"] == True:
                common_ips = i['ips']
                for j in common_ips:
                    if type(ipaddress.ip_network(j)) is ipaddress.IPv6Network:
                        common_ips_set.add(j)
        common_ips_lst = list(common_ips_set)
        common_ips_dic = {'microsoft365CommonAndOfficeOnlineIPv6': common_ips_lst}
        return get_json(common_ips_dic)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


def get_exchange_ipv4():
    """Select items with IP information and in the Exchange service area and
     fill set.

    Usage:
        get_exchange_ipv4()

    :return: JSON with Exchange Online service IPv4 routes
    """
    exchange_ips_set = set()
    try:
        for i in get_data():
            if 'ips' in i and i['serviceArea'] == 'Exchange' and i['expressRoute'] == True:
                exchange_ips = i['ips']
                for j in exchange_ips:
                    if type(ipaddress.ip_network(j)) is ipaddress.IPv4Network:
                        exchange_ips_set.add(j)
        exchange_ips_lst = list(exchange_ips_set)
        exchange_ips_dic = {'exchangeOnlineIPv4': exchange_ips_lst}
        return get_json(exchange_ips_dic)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


def get_exchange_ipv6():
    """Select items with IP information and in the Exchange service area and
    fill set.

    Usage:
        get_exchange_ipv6()

    :return: JSON with Exchange Online service IPv6 routes
    """
    exchange_ips_set = set()
    try:
        for i in get_data():
            if 'ips' in i and i['serviceArea'] == 'Exchange' and i['expressRoute'] == True:
                exchange_ips = i['ips']
                for j in exchange_ips:
                    if type(ipaddress.ip_network(j)) is ipaddress.IPv6Network:
                        exchange_ips_set.add(j)
        exchange_ips_lst = list(exchange_ips_set)
        exchange_ips_dic = {'exchangeOnlineIPv6': exchange_ips_lst}
        return get_json(exchange_ips_dic)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


def get_sharepoint_ipv4():
    """Select items with IP information and in the 'SharePoint' service area
    and fill set.

    Usage:
        get_sharepoint_ipv4()

    :return: JSON with SharePoint Online and OneDrive for Business service IPv4 routes
    """
    sharepoint_ips_set = set()
    try:
        for i in get_data():
            if 'ips' in i and i['serviceArea'] == 'SharePoint' and i['expressRoute'] == True:
                sharepoint_ips = i['ips']
                for j in sharepoint_ips:
                    if type(ipaddress.ip_network(j)) is ipaddress.IPv4Network:
                        sharepoint_ips_set.add(j)
        sharepoint_ips_lst = list(sharepoint_ips_set)
        sharepoint_ips_dic = {'sharePointOnlineAndOneDriveForBusinessIPv4': sharepoint_ips_lst}
        return get_json(sharepoint_ips_dic)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


def get_sharepoint_ipv6():
    """Select items with IP information and in the 'SharePoint' service area
    and fill set.

    Usage:
        get_sharepoint_ipv6()

    :return: JSON with SharePoint Online and OneDrive for Business service IPv6 routes
    """
    sharepoint_ips_set = set()
    try:
        for i in get_data():
            if 'ips' in i and i['serviceArea'] == 'SharePoint' and i['expressRoute'] == True:
                sharepoint_ips = i['ips']
                for j in sharepoint_ips:
                    if type(ipaddress.ip_network(j)) is ipaddress.IPv6Network:
                        sharepoint_ips_set.add(j)
        sharepoint_ips_lst = list(sharepoint_ips_set)
        sharepoint_ips_dic = {'sharePointOnlineAndOneDriveForBusinessIPv6': sharepoint_ips_lst}
        return get_json(sharepoint_ips_dic)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


def get_skype_ipv4():
    skype_ips_set = set()
    try:
        for i in get_data():
            if 'ips' in i and i['serviceArea'] == 'Skype' and i['expressRoute'] == True:
                skype_ips = i['ips']
                for j in skype_ips:
                    if type(ipaddress.ip_network(j)) is ipaddress.IPv4Network:
                        skype_ips_set.add(j)
        skype_ips_lst = list(skype_ips_set)
        skype_ips_dic = {'skypeForBusinessOnlineAndMicrosoftTeamsIPv4': skype_ips_lst}
        return get_json(skype_ips_dic)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


def get_skype_ipv6():
    skype_ips_set = set()
    try:
        for i in get_data():
            if 'ips' in i and i['serviceArea'] == 'Skype' and i['expressRoute'] == True:
                skype_ips = i['ips']
                for j in skype_ips:
                    if type(ipaddress.ip_network(j)) is ipaddress.IPv6Network:
                        skype_ips_set.add(j)
        skype_ips_lst = list(skype_ips_set)
        skype_ips_dic = {'skypeForBusinessOnlineAndMicrosoftTeamsIPv6': skype_ips_lst}
        return get_json(skype_ips_dic)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


def get_exchange_all():
    exchange_all_lst = list()
    try:
        for i in get_data():
            if i['serviceArea'] == 'Exchange':
                exchange_all_lst.append(i)
        exchange_all_dic = {'exchangeOnlineAll': exchange_all_lst}
        return get_json(exchange_all_dic)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


def get_skype_all():
    skype_all_lst = list()
    try:
        for i in get_data():
            if i['serviceArea'] == 'Skype':
                skype_all_lst.append(i)
        skype_all_dic = {'skypeForBusinessOnlineAndMicrosoftTeamsAll': skype_all_lst}
        return get_json(skype_all_dic)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


def get_sharepoint_all():
    sharepoint_all_lst = list()
    try:
        for i in get_data():
            if i['serviceArea'] == 'SharePoint':
                sharepoint_all_lst.append(i)
        sharepoint_all_dic = {'sharePointOnlineAndOneDriveForBusinessAll': sharepoint_all_lst}
        return get_json(sharepoint_all_dic)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


def get_common_all():
    common_all_lst = list()
    try:
        for i in get_data():
            if i['serviceArea'] == 'Common':
                common_all_lst.append(i)
        common_all_dic = {'microsoft365CommonAndOfficeOnlineAll': common_all_lst}
        return get_json(common_all_dic)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


def main():
    #print(get_service_areas())
    #print(get_all_items())
    #print(get_er_exceptions())
    #print(get_items_with_ips())
    #print(get_common_ipv4())
    #print(get_common_ipv6())
    print(get_exchange_ipv4())
    #print(get_exchange_ipv6())
    #print(get_sharepoint_ipv4())
    #print(get_sharepoint_ipv6())
    #print(get_skype_ipv4())
    #print(get_skype_ipv6())
    #print(get_exchange_all())
    #print(get_skype_all())
    #print(get_sharepoint_all())
    #print(get_common_all())

if __name__ == "__main__":
    main()
    
