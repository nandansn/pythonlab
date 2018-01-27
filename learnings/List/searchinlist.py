import reuse

count = reuse.readData()
names = reuse.createNameList(count)


print(names)

checkName = input("Enter name to search:")

print(reuse.searchName(checkName,names))

