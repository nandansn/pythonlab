'''
EEEEE
 DDDD
  CCC
   BB
    A
'''

maxRows = eval(input('Enter Max Rows:'))

startChar = input('Enter start char:')

asciiCodeOfStartChar = ord(startChar)
spaceCount =0
charMultiply = maxRows
for i in range(asciiCodeOfStartChar+maxRows-1, asciiCodeOfStartChar-1, -1):
    print('{}{}'.format(' '*spaceCount,chr(i)*charMultiply))
    charMultiply -= 1
    spaceCount += 1