maxRows = int(input('Enter the rows:'))
startChar = input('Enter start char:')

asciiCodeOfStartChar = ord(startChar)

printPattern = ''

spaceCount = maxRows * 2

for i in range(1,maxRows+1):
    printPattern = ''
    asciiCodeOfStartChar = ord(startChar)
    for k in range(1,i*2,1):
        printPattern = printPattern + chr(asciiCodeOfStartChar)
        asciiCodeOfStartChar += 1
    print('{}{}{}'.format(' '*int(spaceCount/2),printPattern,' '*int(spaceCount/2)))
    spaceCount = spaceCount -2