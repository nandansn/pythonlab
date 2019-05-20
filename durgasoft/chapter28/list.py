'''
insertion order reserved,
hetro objects allowed,
growable,
mutable
'''


'empty list'

ls = []

'dynamic list'

ls = eval(input('enter the list:'))
print(ls)

'nested lists'

ls = eval(input('enter the nested list:'))
print(ls)

'convert sequence into list'

ls = list(range(ord('A'),ord('z')))
print(ls)

'convert string list of char'

print(list('nanda'))

'''accessing list elements, 
    by index
    by slice operator
'''

'slice operator, same as string concept.'

print(list('nanda')[1::1])

'length of list'
print(len([1,2,3]))