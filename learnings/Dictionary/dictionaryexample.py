employee ={"name":"nanda","id":"5300880","salary":"2000"}

print(employee)

# print values only

print(employee.values())

# print keys only
print(employee.keys())

# iterate

for item in employee.items():
    print(item)

# update dictionary
employee["name"] ="kumar"

# add key value
employee.update({"mobile":"9003267101"})
print(employee)

# delete key value
del employee["mobile"]

print(employee)

# clear entire dict
employee.clear()

print(employee)

# delete the dict object from memory

del employee

print(employee)



