maxRows = int(input('Enter max rows:'))

startCharAsciiCode = ord(input('Enter start char:'))

spaceCount = maxRows * 2

printCharPattern = ''

for i in range(1, maxRows+1):
    maxCharRange = i * 2 - 1
    printCharPattern =''
    for k in range(startCharAsciiCode + maxCharRange -1, startCharAsciiCode -1, -1):
        printCharPattern = printCharPattern + chr(k)
    
    print('{}{}{}'.format(' '*int(spaceCount/2), printCharPattern, ' '*int(spaceCount/2)))
    spaceCount = spaceCount -2
