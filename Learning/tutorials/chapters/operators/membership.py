# in and not in are the membership operators in Python.
# They are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary).


list = [1,2,3]

print(" 1 in the list", 1 in list)

tuple = ('nanda','kumar')

print('nanda' in tuple)

print('sekar' not in tuple)

dicty = {1:'nanda',2:'kumar'}

print( 1 in dicty)

# only key is checked for membership
print('nanda' in dicty)
