
import sys

print(sys.getrecursionlimit())

number = eval(input('Enter fact number:'))




def myfact(a):

    if a == 0:
        return 1
    
    return a * myfact(a-1)

print(myfact(number))