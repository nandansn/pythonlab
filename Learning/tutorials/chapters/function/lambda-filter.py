# Example use with filter()

# The filter() function in Python takes in a function and a list as arguments.

# The function is called with all the items in the list and a new list is returned which contains items for which the
# function evaluats to True.

names =['Nanda','kumar','siva','nagu']




new =list(filter(lambda name='': name.__len__() > 4,names))

print(new)



