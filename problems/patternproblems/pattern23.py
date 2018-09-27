'''
EDCBA
EDCB
EDC
ED
E'''

maxNumber = int(input('Enter number:'))

startChar = 'A'

asciiCodeStartChar = ord(startChar)

rangeStartNum = asciiCodeStartChar + maxNumber

patternPrint = ''

count = -1
for i in range(0, maxNumber):
    patternPrint=''
    for j in range(maxNumber -1, count , -1):
        patternPrint = patternPrint + chr(asciiCodeStartChar + j)

    print(patternPrint)
    count += 1