'function: to create empty dict'

d = dict()

'function: to create dict, by using list of tuples'

d= dict([(100,'nanda'),(200,'kumar'),(300,'nivrithi'),(400,'valar')])

print(d)

'''functions: dict()
list of tuples,
set of tuples,
tuple of tuples.
'''

'fucntion:length of dict'

print(len(d))

print(d.get(100))
print(d.get(101)) # if key not present, then none will be returned.
print(d.get(101,'No value')) # o/p will be 'No value'

'to remove the value of the corresponding key'

print(d.pop(100)) # returns the value

print(d)

d.popitem() # key will be chosen randaomly, and corresponding key/value removed and value returned.

print(d)
'to get the keys in the dictionary, returned is not list object. it is dict_keys'
print(d.keys())
'to get only the values, returned is type of dict_values'
print(d.values())
'to get the items(key,value), returned type is dict_items'
print(d.items())

for k,v in d.items() :
    print('key:{}, value:{}'.format(k,v))

d1= d.copy()

print(d1)

'''
if key already avaliable, return the existing value for the key,
if the key unavailable, add the value for that key.return the newly added value.
'''

print(d.setdefault('109','nanda') )
print(d.setdefault('200','jkl'))

print(d)