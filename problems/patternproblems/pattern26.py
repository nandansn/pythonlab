maxNumber = int(input('Enter max number:'))
spaceCount = maxNumber -1
for  i in range(1,maxNumber+1):
    printPattern = str(i) * i
    print((' ' * spaceCount) + printPattern)
    spaceCount -= 1
