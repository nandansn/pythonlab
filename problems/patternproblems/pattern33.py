'''
    ABCDE
     ABCD
      ABC
       AB
        A

'''

maxRows = eval(input('Enter Max Rows:'))

charAppender =''
spaceCount =0

startChar = input('Enter start char:')

asciiCodeOfStartChar = ord(startChar)

for i in range(asciiCodeOfStartChar + maxRows -1, asciiCodeOfStartChar -1, -1):
    charAppender =''
    for c in range(asciiCodeOfStartChar, i+1, 1):
        charAppender = charAppender + chr(c)
    print('{}{}'.format(' '*spaceCount,charAppender))
    spaceCount += 1
