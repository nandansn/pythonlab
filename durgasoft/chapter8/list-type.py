''' list data type 
insertion order is preserved...
duplicates are allowed
hetrogenous objects allowed
list growable
* repetition operator
'''

l=[]
print(type(l))
print(id(l))

l.append(1)
l.append(2)
l.append(3)
l.append(3)
l.append('nan')
l.append(123.45)

print(l)

for i in l:
    print(type(i))
    print(id(i))

print(l[1::2])

print(l*2)