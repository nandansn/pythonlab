maxRowCount = int(input('Enter rows:'))

numberRange = 1


spaceCount = maxRowCount * 2


for i in range(maxRowCount):
    
    printNumber = ''    
    for n in range(1, numberRange+1):
        printNumber = printNumber + str(n)
    numberRange += 2
    print('{}{}{}'.format(' '*int(spaceCount/2),printNumber,' '*int(spaceCount/2)))
    spaceCount = spaceCount - 2
