'''
tuple is immutable.
once tuple created, we r not allowed to perform any changes.
tuple (), paranthesis optional.
'''

daysInWeek = '','Sun','Mon','Tue','Wed','Thu','Fri','Sat'

for day in daysInWeek:
    print('{} is {} day of a week'.format(day, daysInWeek.index(day)))

'''tuple types:
'''

tuphom='A','B','C','C'
print(tuphom)
print(type(tuphom))

tupehetro='1','a'
print(tupehetro)
print(type(tupehetro))


''' list to tuple conversion '''

t=tuple(range(1,30,1))

print(t)

''' slice operatos '''
r=t[-1::-1]

print(r)
    

''' mathematical operators allowed:
+
*
'''

t1 =1,2,3
t2 =2,2,3
print(t1+t2)
print(t1*2)

if (t1 < t2):
    print('equal')
else:
    print('not equal')