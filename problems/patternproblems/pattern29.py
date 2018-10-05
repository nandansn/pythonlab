'''
*****
 ****
  ***
   **
    *
'''

maxNumber = int(input('Enter input number:'))

spaceCount = 0

for i in range(maxNumber,0,-1):
    print(' '*spaceCount+'*'*i)
    spaceCount += 1
