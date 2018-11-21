__author__ = 'rafael'

# Noun => Class
# Adjective => Attributes
# Verb => Method

print('########## Attributes ##########')
class Employee:
    week_hours = 40  # Class attribute; common to all instances of the class

print(Employee.week_hours)

Employee.week_hours = 50  # Modify a class attribute

print(Employee.week_hours)

pito = Employee()
pito.name = 'Rafael'  # Create an instance attribute named name for object pito
pito.week_hours = 45  # Create an instance --not global-- attribute named week_hours
print(pito.name)
print(pito.week_hours)

beto = Employee()
print(beto.week_hours)




class Employee:
    hours = 40  # Class attribute; accessible to all methods via Employee.hours

    def employee_details(self):
        age = 30  # Method attribute; only available to this method for all instances
        self.name = 'Rafael'  # Instance attribute
        print(self.name, age, Employee.hours)  # Accessing attributes (method, instance, & class)

pito = Employee()
pito.employee_details()
print(pito.hours)  # Every instance can access the class attribute via instance.class_attribute
# The two lines above same as Employee.employee_details(pito); that's why self is needed!


print('########## Methods ##########')


class Employee:

    def employee_details(self):  # set value for instance variable name
        self.name = 'Rafael'

    # Static methods do use instance attributes, so no need for self.
    @staticmethod  # Must use this decorator to use static method
    def welcome():   # No need for self since not using it
        print('Hello static method')

pito = Employee()
pito.employee_details()
print(pito.name)
pito.welcome()


# Initialize
class Employee:
    # Is good idea to fully initialize the object
    def __init__(self):  # Initialized instance attribute
        self.name = 'Raf'

    def display_employee_details(self):
        print(self.name)

pito = Employee()
pito.display_employee_details()


# Initialize with class parameter
class Employee:
    # Is good idea to fully initialize the object
    def __init__(self, name):  # Initialized instance attribute
        self.name = name

    def display_employee_details(self):
        print(self.name)

pito = Employee('Rafael')
pito.display_employee_details()