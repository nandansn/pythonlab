''' Pattern:
AAAAA
BBBB
CCC
DD
E
'''

inputChar = str(input('Enter the character:'))

asciiCode = ord(inputChar)

enterIterateNumber = int(input('Enter the number:'))

printIterateNumber = asciiCode + enterIterateNumber + 1

printLineIterateNumber = printIterateNumber
multiplyNumber = enterIterateNumber
for i in range(printIterateNumber - enterIterateNumber-1, printIterateNumber-1):
    consolidate = ''
    for j in range(printIterateNumber - enterIterateNumber-1, printLineIterateNumber-1):
           print(chr(j) * multiplyNumber)
           multiplyNumber = multiplyNumber - 1
    printLineIterateNumber = printIterateNumber - i
    
    