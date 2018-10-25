maxRowCount = int(input('Enter the row count:'))

startChar = 'A'

asciiCodeOfStartChar = ord(startChar)

spaceCount = (maxRowCount * 2) 

charCount = 1

decreaseCount = 2

for i in range(asciiCodeOfStartChar,asciiCodeOfStartChar+maxRowCount):
    print('{}{}{}'.format(' '*int(spaceCount/2),chr(i) * charCount,' '*int(spaceCount/2)))
    charCount += 2
    spaceCount = spaceCount - 2