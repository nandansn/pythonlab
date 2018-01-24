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



