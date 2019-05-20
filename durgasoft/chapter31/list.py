x=[1,2,3,4,9]
y=[1,2,3,4,5]

if (x == y):
    print('true')
else:
    print('false')

z=[1,1,4,5]

'checks the first element and returns the result, if first element of lists are same, then move to next element'
if (x > z):
    print('true')
else:
    print('false')

'membership operator "in" and "not in" '

for i in x:
    if i not in y:
        print('{} not available in list {}'.format(i,y))
        break

'to clear all elements in the list'
x.clear() 
print(x)
