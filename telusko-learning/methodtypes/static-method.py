'''
Static methods, much like class methods, are methods that are bound to a class rather than its object.

They do not require a class instance creation. So, are not dependent on the state of the object.

The difference between a static method and a class method is:

Static method knows nothing about the class and just deals with the parameters.
Class method works with the class since its parameter is always the class itself.

'''

class Calc:
    def printCalc(self):
        print('this is calc')

    @staticmethod
    def addNumbers(x,y):
        print('sum of {} and {} is {}'.format(x,y,x+y))
        


Calc.addNumbers(10,11)