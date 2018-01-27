import reuse

count = reuse.readData()
names = reuse.createNameList(count)


print(names)

# after adding
names.append('e')
print(names)

# after inserting

names.insert(1,'w')
print(names)

# after appending as list
names.append(['v','w','z']) # this will add as list
print(names)

names.extend(['s','r','t'])
print(names)



