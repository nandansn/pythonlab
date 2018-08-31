print("""We have following special operators,
1. identity operator
2. membership operator""")

print("""1. identity operator
a. is
b. not is""")

print (""" Example for is""")

print (""" diff b/w == and is 
is meant for reference check
== meant for value check """)

a=10
b=10

print (a is b)

print (id(a))
print (id(b))

c = 257.12
d = 257.12

print(c is d)

print (id(c))
print (id(d))

e = 'nanda'
f = 'nanda'

print(e is f)

print(id(e))
print(id(f))

ls1 ={10,20,30}
ls2 ={10,20,30}


print (ls1 is ls2)
print (id(ls1))
print (id(ls2))

print (ls1 is not ls2)


print (""" 2. Membership operator
to check the value is member of the object or not
in or not in is applicable for iterable objects""")

ls3 = {10,20,30}

print (30 in ls3)

print (30.0 in ls3)

print (10.1 not in ls3)

name = 'nanda'

print ('a' in name)

tup1 = ('m','t','w','f','s')

print ('z' in tup1)
print ('m' in tup1)

dict1= {1:'n',2:'s'}

print (""" in dictionary in/not in applicable for key only """)
print (1 in dict1)


