import math

def middle_way(a=[], b=[]):
    newNums =[]
    middleOfA = int((len(a) / 2))
    middleOfB =  int((len(b) / 2))
    
    newNums.append(a[middleOfA])
    newNums.append(b[middleOfB])
    return newNums

print(middle_way([1, 2, 3], [4, 5, 6]))
