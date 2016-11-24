
class Program:

    def __init__(self, *args, **kwargs):
        # __init__ automatically runs!
        self.language = input('What language? ')
        self.version = input('What version? ')
        self.skill = input('What skill? ')

    def upgrade(self):
        new_version = input('What is the new version? ')
        # You can reference object's attributes (variables) between methods!
        # Not possible with functions!
        self.version = new_version

p1 = Program()
print(p1.language)
print(p1.version)
print(p1.skill)
p1.upgrade()

p2 = Program()
print(p2.language)
print(p2.version)
print(p2.skill)
p2.upgrade()

print(p1.version)
print(p2.version)