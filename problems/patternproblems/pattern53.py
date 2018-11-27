'''
'''

maxRows = int(input('Enter max rows:'))

startChar = 'A'

unicodeOfStartChar = ord('A')

charFormat = ''

spaces =''

spaceCount = 0
k = 1
for i in range(maxRows, 0, -1):
    
    
    for j in range(0, maxRows * 2 - k ):
        charToPrint = chr(unicodeOfStartChar + j)
        charFormat = (str(charFormat) + str(charToPrint) )
    print('''{0}{1}'''.format(spaces,charFormat))
    spaceCount = spaceCount +1
    spaces = ' ' * spaceCount
    charFormat =''
    k = k +2
  