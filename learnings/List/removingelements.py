import reuse

count = reuse.readData()
names = reuse.createNameList(count)
print(names)

nameToRemove = input("Name to remove:")

# removing a value or multiple values from the list
names.remove(nameToRemove)

print(names)

names.pop()

print(names)

names.clear()

print(names)

del names

print(names)
