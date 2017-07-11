#A dictionary is a data type similar to arrays, but works with keys and values instead of indexes. Each value stored in
#  a dictionary can be accessed using a key, which is any type of object (a string, a number, a list, etc.) instead of
#  using its index to address it.

#initializing the dictionary
employees ={}
employees["1234"] ="Nanda"
employees["1235"] ="Kumar"
employees["1236"] ="Dinesh"
employees["1237"] ="Karthi"

print(employees)

#alternate way to initialize

students ={

    "1234" : "Nanda",
    "1235" : "Kumar",
    "1236" : "Dinesh"
}

print(students)

#iterating dictionaries
for id,name in students.items():
    print("Employee id %s and Employee Name %s" % (id,name))

students.update({"1237" : "Ramesh"})

#removing item from the dictionary.

students.pop("1234")
print(students.__len__())
print(students)

del employees["1234"]

print(employees)


#condition to check the items in the dictionary or not

if "1234" in students:
    print(students.get("1234"))
else:
    print("Student with student id %s not found" % "1234")

if "1235" in students:
     print("Student %s is found"% students.get("1235"))
else:
    print("Student with student id %s not found" % "1235")
