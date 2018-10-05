'''
12345
 1234
  123
   12
    1
'''

maxRows = eval(input('Enter max row number:'))
spaceCount = 0
appendNumbers =''
for i in range(maxRows,0,-1):
    appendNumbers =''
    for n in range(1, i +1):
        appendNumbers = appendNumbers + str(n)
    print('{}{}'.format(' '*spaceCount,appendNumbers))
    spaceCount += 1
