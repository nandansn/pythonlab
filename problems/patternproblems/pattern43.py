maxRows = int(input('Enter the max rows:'))

spaceCount = maxRows * 2

startNum = maxRows - maxRows + 1



for i in range(maxRows):
    printPattern = ''
    if i == 0:
        printPattern ='0'
    else:
        for k in range(i*-1, i+1, 1):
            if k < 0:
                printPattern = printPattern + str(k*-1)
            else:
                printPattern = printPattern + str(k)
    print('{}{}{}'.format(' '*int(spaceCount/2),printPattern,' '*int(spaceCount/2)))
    spaceCount  = spaceCount -2

