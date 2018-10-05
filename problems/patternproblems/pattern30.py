'''
55555
 4444
  333
   22
    1
'''

maxRows = int(input('Enter rows number:'))

spaceCount = 0

for i in range(maxRows,0,-1):
    print('{}{}'.format(' '*spaceCount,str(i)*i))
    spaceCount += 1
