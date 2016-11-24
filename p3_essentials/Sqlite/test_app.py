__author__ = 'rafael'

from element import Element

# Application Title
application = 'myapp.mycompany.com'
print('Checking application [{}]; please wait...'.format(application))

# Element example
hostname = tk = 'google.com'
points = (80, 443)
point_type = 'TCP'
site = 'https://google.com'
element_kind = 'Member Server'

google = Element(element_type=element_kind, node=hostname, ports=points, url=site, kind=point_type)

# print('DEBUG:', google.evaluate())  # Production google.evaluate()
google.evaluate()

'''
from record import record_factory

# Application
app = 'connect.harris.com'

host = 'google.com'
host_type = 'member'
ports = (80, 443)
url = 'http://connect.harris.com'

rec = record_factory(host, host_type, ports, url, port_kind='udp')

print('DEBUG: {}'.format(rec))

print('Application: {}'.format(app))
print('   Element: {}'.format(rec[1]))
print('      Type: {}'.format(rec[2]))
print('      DNS: {}'.format(rec[5]))
print('      Ping: {}'.format(rec[3]))
print('      Ports: {}'.format(rec[4]))
print('      URL: {}'.format(' '.join([url, rec[6]])))

'''
