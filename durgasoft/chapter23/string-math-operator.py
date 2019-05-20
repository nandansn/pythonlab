'''
operators:
+ - concatenation
both the args should be string type only
* - repetition operator
'''

fname = input('enter first name:')

lname = input('enter last name:')
'concat'
print (fname+lname)
'repetition'
print(2 * fname)
print(lname * 2)

print('length of [fname:{} and lname:{}]'.format(len(fname),len(lname)))