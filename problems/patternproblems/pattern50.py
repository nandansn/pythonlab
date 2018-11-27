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

    numberFormat = ''
    for k in range(1,i+1):
        numberFormat = numberFormat + str(k)

    print('''{0}{1}'''.format(spaces,numberFormat))
    numberFormat = ''
    spaces = ' ' * spaceCount
    spaceCount = spaceCount + 1

