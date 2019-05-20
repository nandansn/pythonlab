''' methods of st 
add element, takes one arument
update element, like addAll, takes multiple argument.
copy, does deep copy, creates new set instance.
pop, remove and return the element, removes the some random element.
remove, remove function removes the particular element. if element not available, will get key error.
discard, removes the specified element, if the specified element not available, no error is thrown.
clear, to remove all the elements from the set.
'''

s=set()
s.add(1)
s.add(2)
s.add(3)

print(s)

s.update([1,2,3,4],(9,'k'),'nanda'+'sanmathi')



print(s)

d=s.copy()
print(d)

print(d.pop())

print(d)

print(d.remove('i'))

print(d)