def readData():
    count = input("How many? ")
    return count

def displayList(names=[]):
    for name in names:
        print(name)

def createNameList(count=0):
    names = []
    for i in range(0,int(count)):
        name = input("Enter name:")
        names.append(name)
    return names

def getSlicedList(names=[],a=0,b=0):
    return names[int(a):int(b)]


count = readData()
names = createNameList(int(count))
displayList(names)

# slicing list
slicedNames = getSlicedList(names,0,len(names)/2)

print(slicedNames)

