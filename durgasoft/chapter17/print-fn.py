'repetition of string...'

print('nanda\n'*7)

'concat'

print('nanda'+'kumar')

'variable number of args. default delimiter is space.'

a,b,c=1,2,3

print(a,b,c)

'delimiter'

print(a,b,c,sep=':')

'seperator or delimitor between print statement output, use end.'

print(a,b,c,end='...')
print('nanda')

'formatted string'
a=19
print('amout is %i'%a)
a=90
print('amout is %d'%a)
a=80.9
print('amout is %f'%a)

'multiple values'
a=90
b=40
print('a is %i and b is %i'%(a,b))

'replacement operator'


name,age,location,salary=[str(x) for x in input('Enter value for name, age, location, salary:').split(',')]

print('Name is {0} Age is {1} Salary is {2}'.format(name,age,salary))
