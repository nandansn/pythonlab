'''
function:
    reusable code

module:
    saving set of functions in a file. 
    this file is called module.

package:
    grouping of related modules is called package.

library:
    grouping of related packages is called library.


'''

''' 
types of variables:

    1. global variable: variable declared out side function, available to all modules.
    2. local variable: variable declared inside the function.
    using global keyword inside the function to make the local variable as global.
    by default local variable has high priority.
'''

a=10

def f1():
    # a=999 # local, 
    global a
    a=999
    print (a)

def f2():
    global b
    b = 10
    print(a)

def f3():
    print(b)

def f4():
    a = 90
    print(a)
    print(globals()['a']) # to get the global variable, if the local and global variables have same name.


f1()
f2()
f3()
f4()