import reuse

count = reuse.readData()
names = reuse.createNameList(count)
print(names)

count = reuse.readData()
names2 = reuse.createNameList(count)
names + names2 # 	Lists can also be concatenated with the + operator. 
#list = list + otherlist has the same result as list.extend(otherlist). But the + operator returns a new (concatenated) list as a value, whereas extend only alters an existing list. This means that extend is faster, especially for large lists.

# Python supports the += operator. li += ['two'] is equivalent to li.extend(['two']). The += operator works for lists,
# strings, and integers, and it can be overloaded to work for user-defined classes as well.

names+= names2

print(names)

# The * operator works on lists as a repeater. li = [1, 2] * 3 
# is equivalent to li = [1, 2] + [1, 2] + [1, 2], which concatenates the three lists into one.

print([2,2] * 2)

print ([2,2] - [2])

