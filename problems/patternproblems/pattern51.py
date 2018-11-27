'''
DDDDDDD
 CCCCC
  BBB
   A
'''

maxRows = int(input('Enter max rows:'))

startChar = 'A'

unicodeOfStartChar = ord('A')

charFormat = ''

spaces =''

spaceCount = 0

for i in range(maxRows, 0, -1):
    charToPrint = chr(unicodeOfStartChar + i -1)
    charFormat = (str(charFormat) + str(charToPrint) ) * ((i * 2) -1)

    print('''{0}{1}'''.format(spaces,charFormat))
    spaceCount = spaceCount +1
    spaces = ' ' * spaceCount
    charFormat =''
  