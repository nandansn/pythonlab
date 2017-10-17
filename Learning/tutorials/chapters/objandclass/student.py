# in Python, we define a class using the keyword class.

# A class creates a new local namespace where all its attributes are defined. Attributes may be data or functions.

# As soon as we define a class, a new class object is created with the same name. This class object allows us to access
#  the different attributes as well as to instantiate new objects of that class.

class Student:
    ''' This is student class'''
    name = ""

    def display(self):

        print(self.name)

    def __init__(self,str):
        print("object initialization")
        self.name = str

print(Student.name)

print(Student.display)

print(Student.__doc__)

obj = Student("nanda")

# You may have noticed the self parameter in function definition inside the class but,
#  we called the method simply as ob.func() without any arguments. It still worked.

# This is because, whenever an object calls its method, the object itself is passed as the first argument.
#  So, ob.func() translates into MyClass.func(ob).

obj.display()

# Deleting Attributes and Objects

del obj.name

del Student.display

obj.display()
