'''
A
AB
ABC
ABCD
ABCDE
'''

enterMaxNumber = int(input('Enter Number:'))

enterStartChar = input('Enter start char:')

asciiCodeOfStartChar = ord(enterStartChar)

endRange = asciiCodeOfStartChar +enterMaxNumber

printChars =''
spaceCount = 4
for i in range(asciiCodeOfStartChar,endRange):
    printChars = printChars + chr(i)
    print(' '*spaceCount,printChars)
    spaceCount -= 1

