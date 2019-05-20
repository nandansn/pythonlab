'''
update dictionary,
'''

d = {101:'durga',102:'shiva'}

d[103] = 'kumar' #if key not there, new value will be added.

d[101]='nanda' #if key already available, new value will be updated.

print(d)

' how to delete elements from the dictionary '

del d[101] # if the key present, then the key and value will be removed

print(d)

try:
    del d[101]
except KeyError as key:
    print('key {} not available in {}'.format(key,d))

d.clear()
' to clear all the key/value pairs in dict'

print(d)

d.update({101:'abc'})



try:
    del d # this object is available for garbage collection.
except NameError as name:
    print ('{} is not defined'.format(name))


'how to speciy multiple values for the key'

a={}

a[100]=['nanda','kumar','k']

print(a)

