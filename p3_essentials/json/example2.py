import requests
from ipaddress import IPv4Network

guid = '3217a7be-6b61-40b4-8565-6e9fd2b76729'
url = 'https://endpoints.office.com/endpoints/USGovGCCHigh/?ClientRequestId='
uri = url+guid

response = requests.get(uri)
json_data = response.json() # type list

exchange = 'Exchange Online'
skype_teams = 'Skype for Business Online and Microsoft Teams'
sharepoint_onedrive = 'SharePoint Online and OneDrive for Business'
o365_common = 'Microsoft 365 Common and Office Online'


def create_set(kind=None):
    container = set()
    for d in json_data:
        for i in d:
            if kind is None:
                if i == 'ips':
                    ls = d['ips']
                    for j in ls:
                        if ':' not in j:
                            container.add(j)
            else:
                if i == 'ips' and d['serviceAreaDisplayName'] == kind:
                    ls = d['ips']
                    for j in ls:
                        if ':' not in j:
                            container.add(j)
    print(container)
    print(len(container))
    return container


def create_routes(container):
    pass

create_set(sharepoint_onedrive)

cidr = '23.103.191.0/24'
print(IPv4Network(cidr).network_address, IPv4Network(cidr).netmask)

'''
for d in json_data:
    for i in d:
        if i == 'ips':
            service = d['serviceAreaDisplayName']
            ls = d['ips']
            lst = [x for x in ls if ':' not in x]
            print(service)
            print(lst)


container = []
for d in json_data:
    for i in d:
        if i == 'ips' and d['serviceAreaDisplayName'] == o365_common:
            print(d['serviceAreaDisplayName'])
            ls = d['ips']
            lst = [x for x in ls if ':' not in x]
            container.extend(lst)
container_set = set(container)
print(container_set)
print(len(container_set))
'''