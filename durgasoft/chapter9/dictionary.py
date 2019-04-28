'''
dictionary is a map
key, value pair.
key is unique.
value, duplicates allowed
dict is a mutable
'''

kv = {1:'nanda'}

print(kv)

for key in kv:
    print(kv[key])

kv.update({2:'sanmathi'})

for k,v in kv.items():
    print(k,v)
