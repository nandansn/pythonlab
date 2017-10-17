# Python has many built-in exceptions which forces your program to output an error when something in it goes wrong.

import sys

try:
    number = input("Enter Number:")
    div = 100 / number
except:
    print('something went wrong!!!')
    print(sys.exc_info())


try:
    number = input("Enter Number:")
    div = 100 / int(number)
    print(div)
except TypeError:
    print('something went wrong!!!')
    print('entered type is not number')

finally:
    print("closing the task")

# In Python programming, exceptions are raised when corresponding errors occur at run time,
#  but we can forcefully raise it using the keyword raise.

try:
    names = input("Enter Name:")

    if names.__len__() < 3:
        raise ValueError("Name lenght is less than 3")

except ValueError as e:
    print(e.args)


finally:
    pass

# User-Defined Exception

class NameLengthException(Exception):
    pass

try:
    names = input("Enter Name:")

    if names.__len__() < 8:
        raise NameLengthException("Name lenght is less than 8")

except NameLengthException as e:
    print(e.args)


finally:
    pass
