maxNumber = int(input('Enter number:'))

starCount = 1
for i in range(maxNumber,0,-1):
    strprint = ' '*i
    print(strprint+'*'*starCount)
    starCount += 1