maxRows = int(input('Enter the rows:'))

spaceCount = maxRows * 2

numberPattern = ''

for i in range(1,maxRows+1):
    numberPattern =''
    for num in range(i*2-1,0,-1):
        numberPattern = numberPattern + str(num)
    print('{}{}{}'.format(' '*int(spaceCount/2),numberPattern,' '*int(spaceCount/2)))
    spaceCount = spaceCount -2