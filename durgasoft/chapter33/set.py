'''
{}
no order manintained,
duplicates not allowed
cannot accessed by indexing
mutable
empty {}, treated as dictionary, not as set.
indexing or slicing not applicable for the set
'''

s={1,2,3,4}

print(type(s))

s.add(123)

print(s)

s.add(123)

print(s)

print(type({})) #treated as dictionary

'to create empty set'

print(type(set({})))

print(set('nanda'))
