######## Object Oriented Programing ########

#### General OOP ####
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

s1 = Student('Tim', 19, 95)
s2 = Student('Bill', 19, 75)
s3 = Student('Jill', 19, 65)

course = Course('Science', 2)
course.add_student(s1)
course.add_student(s2)

print(course.students) # List of Student objects
print(course.students[0].name) # Student object name attribute
print(course.get_average_grade())
print(course.add_student(s3)) # Will return False becouse student max is 2

#### Inheritance ####
class Pet():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'Iam {self.name} and I am {self.age} years old.')

    def speak(self): # This method speak is overriden by Cats's speak method.
        print('I dont know what to say')

class Cat(Pet):
    def __init__(self, name, age, color): #  Need it to add color atribute to Cat object
        super().__init__(name, age) # Needed to continue using parent's init attributes
        self.color = color

    def speak(self):
        print('meow')

    def show(self):
        print(f'I am {self.name}, I am {self.age} years old and my color is {self.color}')

class Dog(Pet):
    def speak(self):
        print('Bark')

class Fish(Pet):
    pass

p = Pet('Tim', 19)
p.show()

c = Cat('Bill', 34, 'blue')
c.show() # Inherit method show() from class Pet
c.speak()

d = Dog('Jill', 25)
d.show()
d.speak()

f = Fish('bubbles', 10)
f.speak() # Will use parent speak method becouse a method speak is not defined in Fish class.

#### Class attributes ####
# An attr that is applicatble to all instances
class Person():
    number_of_people = 0

    def __init__(self, name):
        self.name = name

p1 = Person('Jim')
p2 = Person('Jill')

# Python first chech if the instance has the attribute, if it doesn't, then check the class
print(Person.number_of_people) # 0
print(p2.number_of_people) # 0
Person.number_of_people = 8
print(p2.number_of_people) # 8

# Class attribute real world example
class Person():
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1

p1 = Person('Jim')
p2 = Person('Jill')
print(Person.number_of_people) # 2

#### Class Methods,no access to instance ####
class Person():
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person() # Will execute this class method during init

    @classmethod
    def total_people(cls): # Only access to class attr not instance attr
        return cls.number_of_people

    @classmethod
    def add_person(cls): # Only access to class attr not instance attr
        cls.number_of_people += 1

p1 = Person('Jim')
p2 = Person('Jill')
print(Person.number_of_people) # 2
print(Person.total_people()) # 2

#### Stactic methods not specific to an instance just grouped in a class ####
# Static methods don't change anything
class Math:

    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

print(Math.add5(3)) # 8
print(Math.add10(3)) # 13
