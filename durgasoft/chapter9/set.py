'''
set:
duplicates not allowed.
insertion order not preserved.
mutable.
indexing, slice operator not valid in set.
hetrogenous objects allowed
'''

s = {10,20,30,40}

for i in s:
    print(i)

for i in range(100,200,10):
    s.add(i)

for i in s:
    print(i)

print(s)

k = {10,20,99}

print(k.difference(s))

print(k.union(s))

print(k.intersection(s))

print(s.add('nanda'))

print(s)