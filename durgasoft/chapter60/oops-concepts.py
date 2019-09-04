'''
class:
    blueprint or plan or design.
object:    
    physical existence of the class.
reference variable:
    used to refer the object, used to operate the object, like a pointer.

how to define a class?
    class contains?
        data/variables/state of the object.
        methods/behaviour of the object.

class Employee: 
    pass

e = Employee()

# classname starts with uppercase.

metohds in the class, within the class any function is referred as method.
    method should take mandatory argument called self, self is like this keyword in python.
    you can use any argname instead of self, but using self is good programming convention.


Constructor in python:
    purpose:
        to perform initialization of objects.
        instance variable initializtion.

def __init__(self):
        pass

variables whose values, varies from object to object is called instance variables.

3 types of variables,
    static variables
    non-static variables
    local variables

3 types of methods,
    static methods
    non-static methods
    class methods

'''

class Employee:
    ''' This is employee class '''
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def display(self):
        print('working in oracle...')
        print('Name:{0}\nAge:{1}\nSalary:{2}'.format(self.name,self.age,self.salary))



e = Employee('Nanda',24,120000000)
e.display()
print(e) # <__main__.Employee object at 0x00D6C4D0>
print(help(Employee)) # will display the class information.

print(Employee.__doc__) # displays the doc, about the class.

