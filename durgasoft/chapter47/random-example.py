from random import *

for i in range(10):
    print(random())

for i in range(10):
    print(randint(i,567)) # generat the int value, inclusive of start and end.

for i in range(10):
    print(uniform(i,10)) #generate the float value, within the range. not inclusive of start and end values.

for i in range(10):
    print('random numbers')
    print(randrange(1,11,3)) # generate the random number with step value