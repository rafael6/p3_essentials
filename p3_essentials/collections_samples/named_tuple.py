# Traditional tuple

t = (1, 2, 3)
print(t[0])

from collections import namedtuple

# Assigns a name and a dlice index to each element
dog = namedtuple('Dog', 'age breed name')  # Note spaces between the fields
lala = dog(age=2, breed='Tarrier', name='Lala')

print(lala)  # Dog(age=2, breed='Tarrier', name='Lala')
print(lala.age)  # 2
print(lala[0])  # 2
