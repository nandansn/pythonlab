'''
   1
  121
 12321
1234321
'''

maxRows = int(input('enter max rows:'))

spaceCount = maxRows - 1
spaces = ' ' * spaceCount

numbersFormat = ''
j =1

for i in range(1,maxRows+1):
    numbersFormat = ''
    for j in range(1, i):
        numbersFormat = numbersFormat + str(j)
    for k in range(i,0,-1):
        numbersFormat = numbersFormat + str(k)

    print('''{0}{1}'''.format(spaces,numbersFormat))
    spaceCount = spaceCount -1
    spaces =' ' * spaceCount
