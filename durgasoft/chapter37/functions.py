'''
functions: code reusability,
2 types of functions,
    1. pre-defined/in-built functions
    2. user definded functions
'''

def display():
    print('function: code reusability')

def day():
    return 'sunday'

display()
print(day())

def display_name(name):
    print(name)

display_name('nanda')

'function can return multiple vvalues...'

def multiple_values():
    return 1,2,3

x,y,z = multiple_values() # default return type is tuple.

t = x,y,z

print(t)

'''types of arguments
    positional
    keyword
    default
    variable-length
'''