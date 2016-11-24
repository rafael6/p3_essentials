# Traditional dict

d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5
for k,v in d.items():
    print(k,v)

print()

from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
od['e'] = 5
for k,v in od.items():
    print(k,v)

print()

# The orders of how items are added matters, the comparizon statement is False
od1 = OrderedDict()
od1['a'] = 1
od1['b'] = 2
od1['c'] = 3

od2 = OrderedDict()
od2['c'] = 1
od2['b'] = 2
od2['a'] = 3

print(od1 == od2)