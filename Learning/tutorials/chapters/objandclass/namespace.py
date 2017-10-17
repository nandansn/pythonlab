a = 2;
print(id(a))

a = 3;

#This is efficient as Python doesn't have to create a new duplicate object.
# This dynamic nature of name binding makes Python powerful; a name could refer to any type of object.

#  you can imagine a namespace as a mapping of every name, you have defined, to corresponding objects.

# A namespace containing all the built-in names is created when we start the Python interpreter and exists as long we don't exit.

b = 2;

print(id(a))


print(id(b))
