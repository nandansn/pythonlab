# python default arguments
# non-default arguments cannot follow default arguments.
def greet(name,msg="welcome to python world"):
    print (name,msg)

greet("nanda")
greet("kumar","how are you")

# Python Keyword Arguments

# When we call a function with some values, these values get assigned to the arguments according to their position

# But we must keep in mind that keyword arguments must follow positional arguments.

greet(name="sanmathi",msg="good today!")
greet(msg="good day!",name="nivrithi")

# Python Arbitrary Arguments

# Sometimes, we do not know in advance the number of arguments that will be passed into a function.
# Python allows us to handle this kind of situation through function calls with arbitrary number of arguments.

# In the function definition we use an asterisk (*) before the parameter name to denote this kind of argument

def addNumbers(*numbers):
    s = 0
    for number in numbers:
        s = s + number
    return s

print("sum is ",addNumbers(1,2,3,4,5,6))
