print(''' all fundamental datatypes are immutable''')

x = 10
print(x)
print(id(x))
x = 11 
''' new object will be created. old object will still remain in the memory. 
if in future any variable want to use 10, then that object assigned to that variable. 
object reusability. improves the performance. '''

''' immutable data types:
int
float
bool
complex
str
'''
y=10
print(id(y))

print(id(x))

del(x)
print(x)