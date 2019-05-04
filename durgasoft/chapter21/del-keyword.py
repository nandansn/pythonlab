'''
del is a keyword python.
del used for garbaage collection.

'''

''' example: '''

name ='nanda'
del name

#print (name)

l = [1,2,3,4,5]
b = bytearray(l)
print(b)

del b[1]

print(b[1])

s='nanda'
#del s[0] #string is immutable

'''
del and None

del -> value and reference variable will be deleted.
None -> value will be deleted. reference will be there.

'''

s=None

print(s)

'''
in the below example, value remains, because other variables are referring to the value or object
'''

a=10
b=10
c=10

print(a,b,c)


del a


print(b,c)