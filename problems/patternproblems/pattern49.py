'''
33333
 222
  1
  '''

maxRows = int(input('Enter max rows:'))

numberFormat = ''
spaces =''
spaceCount = 1
for i in range((maxRows * 2 -1),-1,-2):
    k = i
    numberFormat = numberFormat + str(i) * (i)
    print('''{0}{1}'''.format(spaces,numberFormat))
    numberFormat = ''
    spaces = ' ' * spaceCount
    spaceCount = spaceCount + 1

