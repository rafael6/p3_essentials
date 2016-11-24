#!/usr/bin/env python3

__author__ = 'rafael'
__version__ = '1.0.0'

"""
Dispatch and format output.

>>> from element import Element
>>> application = 'myapp.mycompany.com'
>>> hostname = 'google.com'
>>> points = (80, 443)
>>> point_type = 'UDP'
>>> site = 'https://google.com'
>>> element_kind = 'Member Server'
>>> google = Element(element_type=element_kind, node=hostname, ports=points, url=site, kind=point_type)
>>> google.evaluate()
   Element: [google.com]
      Type=[Member Server]
      Record=[google.com] Resolution=[216.58.192.110]
      Host=[google.com] Ping=[0% packet loss]
      Type=[UDP] Socket=[google.com]:[80] Status=[open]
      Type=[UDP] Socket=[google.com]:[443] Status=[open]
      URI=[https://google.com] Status=[200]
>>>
"""

__author__ = 'rafael'

from toolkit import Toolkit
from datetime import datetime


class Element(Toolkit):
    def __init__(self, element_type=None, ports=None, node=None, port=None, url=None, kind='tcp'):
        super().__init__(node, port, url, kind)
        self.element_type = element_type
        self.ports = ports

    def check_host(self):
        """Calls Toolkit.check_host() and format/prints the returned value.
        """
        _output = super().check_host()
        try:
            _filter = _output.split('received, ')[1]  # 0% packet loss, time 1606ms...
            _refined = _filter[0:16].strip(', ')      # 0% packet loss
            return _refined
        except IndexError as e:
            return 'connection error'

    def check_socket(self):
        """Calls Toolkit.check_socket() and format/prints the returned value.
        """
        _output = []
        for port in self.ports:
            self.port = port
            _result = super().check_socket()
            _port_stat = [self.kind, str(self.port), _result]
            _output.append(' '.join(_port_stat))
        return _output

    def merge_dicts(self, *dict_args):
        """Given any number of dicts, shallow copy and merge into a new dict,
        precedence goes to key value pairs in latter dicts."""
        result = {}
        for dictionary in dict_args:
            result.update(dictionary)
        return result

    def evaluate(self):
        """Dispatch the following methods:
                check_dns(),
                check_host(),
                check_socket(),
                check_url()
                """
        _resolution = super().check_dns()
        _ping = self.check_host()
        _ports = ', '.join(self.check_socket())
        _code = super().check_url()
        _url = ' '.join([self.url, str(_code)])


        print('   Element: {}'.format(self.node))
        print('      Type: {}'.format(self.element_type))
        print('      DNS: {}'.format(_resolution))
        print('      Ping: {}'.format(_ping))
        print('      Ports: {}'.format(_ports))
        print('      URL: {}'.format(_url))

        # DATA BASE CALLS
        print()

        db_timestamp = dict([('date_time', str(datetime.now()))])
        print(db_timestamp)

        db_element = dict([('ip_element', self.node)])
        print(db_element)

        db_type = dict([('element_type', self.kind)])
        print(db_type)

        db_dns = dict([('dns_status', _resolution)])
        print(db_dns)

        db_ping = dict([('ping_status', _ping)])
        print(db_ping)

        db_port = dict([('port_status', _ports)])
        print(db_port)

        db_url = dict([('url_status', _url)])
        print(db_url)

        new_dict = self.merge_dicts(db_timestamp, db_element, db_type, db_dns, db_ping, db_port, db_url)
        print(new_dict)


        # DEBUG
        #return str(datetime.today()), self.node, self.element_type,\
              # _resolution, _ping, _ports, _url

def main():
    # Application
    application = 'myapp.mycompan.com'

    # Element attributes
    element_kind = 'Member Server'
    hostname = 'yahoo.com'
    points = (80, 443)
    site = 'https://google.com'

    print('Checking application [{}]; please wait...'.format(application))

    google = Element(element_type=element_kind, node=hostname, ports=points, url=site)
    google.evaluate()


if __name__ == '__main__':
    main()

