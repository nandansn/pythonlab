
'apply the expression on each value on the range and return the list.'
l=[x*x for x in range(1,11)] 

print(l)

'adding condition [expression for x in range if condition] and if condition is true apply the expression'

l2 = [x*x for x in range(1,21)if  x%2==0]
print(l2)

'applying multiple expressions'

l3 = ['nanda','kumar','sanmathi','nivrithi']

l4 = [[w, len(w), 'starts with letter - {}'.format(w[0])] for w in l3]

print(l4)
