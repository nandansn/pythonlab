'''
1
222
33333
'''

maxRows = eval(input('Enter max rows:'))

spaceCount = int((maxRows*2)) - 1

numberCount = 1

for i in range(1,maxRows+1):
    
    print('{}{}{}'.format(' '*int((spaceCount - numberCount )/2),str(i)*numberCount,' '*int((spaceCount - numberCount )/2)))
    numberCount += 2