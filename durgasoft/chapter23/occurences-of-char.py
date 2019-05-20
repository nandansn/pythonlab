name = input('Enter name:')

occur = {}
counter =0

for i in range(len(name)):
    if name[i] in name[i:]:
        if occur.get(name[i]) == None:
            occur.update({name[i]:1})
        else:
            counter = occur.get(name[i])
            occur.update({name[i]:counter+1})

print(occur)