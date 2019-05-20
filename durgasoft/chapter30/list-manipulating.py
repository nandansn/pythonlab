'''
remove element from list
if specified element not found in the list, we will get, value error.
pop()- 
removes the list element and returns that element.
if element not found, error: pop from empty list.
pop(index)
-remove the element at the index.
IndexError: pop index out of range if element not found in the index.
'''

ls = [1,2,3]

ls.remove(1)

print(ls)

print(ls.pop())

ls = ls + [4,5,6,7,8]

print(ls.pop(4))


''' 
ordering the element of the list.
'''

ls = [4,5,6,3,2,1]

ls.reverse()

print(ls)

'''
sort method
default natural sorting order:
numbers - ascending order
chars - alphabetical order or unicode
hetrogenous not allowed in sorting method.
'''

ls.sort()

print(ls)

ls=list('nanda')

ls.sort()

print(ls)

ls =['z','A','a',1000]

# ls.sort() # TypeError: '<' not supported between instances of 'int' and 'str'

print(ls)


'deep copy: using slice operator or copy method'

ls1 = ls[:]

ls1.append('e')
ls2 = ls.copy()
ls2.remove('A')

print('ls:{} ls1: {} ls2: {}'.format(ls,ls1,ls2))