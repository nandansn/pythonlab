from array import *

intArray = array('i',[])

intLength = eval(input("Enter length of array"))

for i in range(intLength):
    intValue = eval(input("Enter the value:"))
    intArray.append(intValue)

for i in range(len(intArray)):
    print(intArray[i])