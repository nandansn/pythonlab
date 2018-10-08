'''
default argument
variable args
kwargs
'''

from functools import reduce

# default args example
def sum(a=10,b=20):
    print(a+b)

sum()
sum(11,12)

# variable args
def multiply(*numbers):
    print(type(numbers))
    print(reduce(lambda x,y: x *y,numbers))

multiply(1,2,3,4)

# keyword args
def person(**personData):
    print(type(personData))
    print(personData.get('name'))

person(name='sanmathi',age='32')