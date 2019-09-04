'''
filter functions,
syntax:filter(function,sequence/list)
'''

even=lambda i : True if i%2 == 0 else False

'filter the elements that returns true, after applying the functions on the list of elements.'
print(list(filter(even,[1,2,3,4]))) 


print(list(filter(lambda i: True if i%2 != 0 else False,[1,2,3,4]))) 
