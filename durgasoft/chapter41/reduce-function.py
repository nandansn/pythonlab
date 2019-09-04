'''
reduce():reducing the sequence of values to single value
'''

import functools

l1=[1,2,3,4,5,6]

print(functools.reduce(lambda i,j: i + j,l1))
