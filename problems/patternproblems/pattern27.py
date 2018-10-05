'''
    A
   BB
  CCC
 DDDD
EEEEE

'''

maxNumber = 5
startingChar ='A'

asciiCodeOfChar = ord('A')
count = 0
multiChar = 1
for i in range(5,0,-1):
    print(' '*i, chr(asciiCodeOfChar + count) * multiChar)
    count += 1
    multiChar += 1

