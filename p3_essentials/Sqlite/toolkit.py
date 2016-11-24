#!/usr/bin/env python3
__author__ = 'rafael'
__version__ = '1.1.0'

"""
This modules provides methods for checking: ICMP/DNS, sockets, and URL status.

>>> from toolkit import Toolkit
>>> app = Toolkit(node='google.com', port=80, url='http://google.com')
>>> print(app.check_dns())
('google.com', '216.58.192.78')
>>> print(app.check_host())
--- google.com ping statistics ---
9 packets transmitted, 9 received, 0% packet loss, time 1610ms
rtt min/avg/max/mdev = 57.245/59.731/70.123/3.753 ms
>>> print(app.check_socket())
('google.com', 80, 'tcp', 'open')
>>> print(app.check_url())
('http://google.com', '200')
"""

import socket
import subprocess
import urllib.request


class Toolkit:
    """This class contains the following methods: check_dns(), check_host(),
    check_socket()and check_url().
    """
    def __init__(self, node=None, port=None, url=None, kind='tcp', count='9'):
        self.node = node
        self.port = port
        self.url = url
        self.kind = kind
        self.count = count
        self.output = None

    def check_dns(self):
        """Return a given hostname and its DNS name resolution as a tuple:
            (hostname, IP address) otherwise an exception.
        """
        try:
            output = socket.gethostbyname(self.node)
            if output:
                #return self.node, output
                return output
        except socket.gaierror as e:
            return '{}'.format(e)

    def check_host(self):
        """Ping a given node by its name or IP address with a load of 1378
        bytes, a given number of times (default 9), at a 200ms interval.
        Returns a ping statistics, otherwise an exception
        """
        _interval = '.2'  # 200ms
        _size = '1350'    # bytes
        _command = 'ping -c {} -i {} -s {} {} | grep -1 loss'.format(
            self.count, _interval, _size, self.node)
        try:
            self.output = subprocess.check_output(_command, shell=True)\
                .decode('utf-8').strip()
            return self.output
        except subprocess.CalledProcessError as e:
            return '{}'.format(e)

    def check_socket(self):
        """Check the status of a given socket (hostname, ports) as arguments.
        Returns a tuple:
            (hostname, port, port type, open if port is open) otherwise an exception
         """
        if self.kind == 'udp' or self.kind == 'UDP':
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect((self.node, self.port))
            self.sock.close()
        except socket.error as e:
            return '{}'.format(e)
        except OverflowError as e:
            return '{}'.format(e)
        else:
            return 'open'

    def check_url(self):
        """Check the status of a given URL.
        Returns a tuple:
            (url, http code) otherwise an exception
        """
        try:
            self.connection = urllib.request.urlopen(self.url)
        except urllib.error.URLError as e:
            return '{}'.format(e)
        except ValueError as e:
            return '{}'.format(e)
        else:
            return str(self.connection.getcode())


def main():
    tk = Toolkit('google.com', port=80, url='https://google.com')
    print(tk.check_dns())
    print()
    print(tk.check_host())
    print()
    print(tk.check_socket())
    print()
    print(tk.check_url())

if __name__ == "__main__":
    main()
