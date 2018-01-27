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

def searchName(name="",names=[]):
    if name in names:
        return name+ " found in the list."
    else:
        return name+ " not found in the list."
