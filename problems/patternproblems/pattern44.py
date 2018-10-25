maxRows = int(input('Enter max rows:'))


startChar = 'A'

asciiCodeOfStartChar = ord(startChar)

printPattern = ''

spaceCount = maxRows * 2

chars =''

for i in range(maxRows):
    printPattern = ''
    if i == 0:
        printPattern = printPattern + startChar
    else:
        chars =''
        for k in range(i * -1, i +1, 1):
            if k < 0:
                chars = chars + chr(asciiCodeOfStartChar + (k * -1))
            else:
                chars = chars + chr(asciiCodeOfStartChar + (k * 1))
    printPattern = printPattern + chars
    print('{}{}{}'.format(' '*int(spaceCount/2),printPattern,' '*int(spaceCount/2)))
    spaceCount = spaceCount -2


