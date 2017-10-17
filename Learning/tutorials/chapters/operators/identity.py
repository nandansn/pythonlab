# is and is not are the identity operators in Python.
# They are used to check if two values (or variables) are located on the same part of the memory.

x ="hello"
y ="hello"

print("x is y", x is y)

y = "Hello"

print("x is y", x is y)

print(" x is not y", x is not y)


x = [1,2,3]
y = [1,2,3]

print("x is not y", x is not y)
