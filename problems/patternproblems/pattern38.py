maxRows = int(input('Enter max rows:'))

charCount = 1

startChar = 'A'

asciiCodeStartChar = ord(startChar)


spaceCount = (maxRows - 1) * 2



for i in range(asciiCodeStartChar, (asciiCodeStartChar + maxRows * 2), 2):
    
    print('{}{}{}'.format(' '*int(spaceCount/2),chr(i)*charCount,' '*int(spaceCount/2)))
    spaceCount = spaceCount - 2
    charCount += 2