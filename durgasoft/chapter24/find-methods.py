'''
find()
index()

will return the index of the first matched substring in the string....

rfind()
rindex()

check for the substring in the string from right....

if the substring is available then find()/rfind() and index()/rindex() returns index value, else
find()/rfind() returns -1 and index()/rindex() returns value not found error
'''

name ='nandakumarsanmathi'

print(name.find('a'))
print(name.rfind('a'))


print(name.find('o'))
print(name.rfind('o'))

# print(name.index('o')) # will return, ValueError: substring not found
print(name.rindex('o')) # will return, ValueError: substring not found
