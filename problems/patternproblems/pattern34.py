'''
  *
 ***
*****

'''

numberOfRows = int(input('Enter rows:'))

maxStars = (numberOfRows * 2) - 1

starCount = 1

for i in range(0,numberOfRows):
    print('{}{}{}'.format(' '*int((maxStars-1)/2),'*'*starCount,' '*int((maxStars-1)/2)))
    starCount += 2
    maxStars += -2