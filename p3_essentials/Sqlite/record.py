#!/usr/bin/env python3

__author__ = 'rafael'
__version__ = '1.0.0'

from datetime import datetime
from toolkit import Toolkit


def record_factory(host, host_type, ports, url, port_kind='tcp'):

    l = []
    for p in ports:
        i = Toolkit(host, p, url, port_kind)
        field = '{} {} {}'.format(port_kind, p, i.check_socket())
        l.append(field)
        port_status = ', '.join(l)

    _output = i.check_host()
    _filter = _output.split('received, ')[1]  # 0% packet loss, time 1606ms...
    ping_status = _filter[0:16].strip(', ')      # 0% packet loss

    timestamp = datetime.today()

    dns_status = i.check_dns()

    url_status = i.check_url()

    return str(timestamp), host, host_type, ping_status, port_status, dns_status, url_status


def main():
    host = 'google.com'
    host_type = 'member'
    ports = (80, 443)
    url = 'http://connect.harris.com'
    port_kind = 'tcp'
    print(record_factory(host, host_type, ports, url, port_kind))


if __name__ == "__main__":
    main()
