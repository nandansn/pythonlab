'''
Types of exceptions,
1. Pre-defined/System Defined Exceptions
2. User Defined/Customized exceptions

1. Pre-defined/System Defined Exceptions,
    in risky condition or event, python raise the exception.

    example: print(10/0) ZeroDivisionError

2. User Defined Exception,

    we will raise exception from the program.
    How to define and raise user defined exception....
    

class AgeInvalidException(Exception):
    def __init__(self,message):
        self.msg = message


'''

