''' functions of tuple: '''

'len()'

t = tuple(input('enter tuple:'))

print(t)
print(len(t))

'count occurence of the elelement'

print(t.count('1'))

'''sorting:
    natural sorting order
'''

t=(4,3,2,1)
print(sorted(t))
print(tuple(sorted(t)))
print(tuple(sorted(t,reverse=True)))

'min and max method to find in the tuple...'

print(max(t))
print(min(t))




