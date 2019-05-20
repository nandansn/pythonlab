name = input('enter name:')

noDuplicates = ''


for i in range(len(name)):
    if name[i] not in noDuplicates:
        noDuplicates = noDuplicates + name[i]

name = None
name = noDuplicates

print(name)
