intMaxRows = int(input('Enter max rows:'))


spaceCount = intMaxRows * 2 - 2


for i in range(1,intMaxRows*2+1,2):
    print('{}{}{}'.format(' '*int(spaceCount/2),str(i)*i,' '*int(spaceCount/2)))
    spaceCount = spaceCount - 2