'''
key,value pair
empty dict {}
dict are dynamic,
indexing/slicing not available in dict
no key duplicates
value can be dulpicated.
for keys and values, hetrogenous objects allowed.
'''

d={}
d=dict()
d[1]='nanda'

d.update({2:'kumar'})

d['mob']=9003267101
print(d)

'access element'

print(d[1])
try:
    print(d[3]) #key not available, we will get key error
except KeyError as e:
    print(e)
