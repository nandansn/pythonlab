'''
  A
 ABA
ABCBA
'''

maxRows = int(input('Enter max rows:'''))

spaceCount = maxRows - 1

spaces = ' ' * spaceCount

startChar = 'A'

unicodeOfStartChar = ord(startChar) - 1

charFormat = ''
for i in range(1, maxRows+1):
    charFormat = ''
    for j in range(1,i):
        charFormat = charFormat + chr((unicodeOfStartChar + j))
    for k in range(i,0,-1):
        charFormat = charFormat + chr((unicodeOfStartChar + k))
    
    print('''{0}{1}'''.format(spaces,charFormat))
    spaceCount = spaceCount - 1
    spaces = ' ' * spaceCount