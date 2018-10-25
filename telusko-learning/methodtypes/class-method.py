'''

A class method is a method that is bound to a class rather than its object. It doesn't require creation of a class instance, much like staticmethod.

The difference between a static method and a class method is:

Static method knows nothing about the class and just deals with the parameters
Class method works with the class since its parameter is always the class itself.

'''

class Employee:

    companyName = 'NIVRI Corp'

    def __init__(self,name):
        self.name = name

    @classmethod
    def printCompanyName(cls):
        print('Company Name is {}'.format(cls.companyName))
        

    
Employee.printCompanyName()