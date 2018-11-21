
# ID, Moving the variable (pointer) to different string objects
my_string = "abc"
print(id(my_string))

my_string = "def"
print(id(my_string))

my_string = my_string + "ghi"
print(id(my_string))

