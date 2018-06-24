filePath = open("C:\\Users\\nrangasa.ORADEV\\git\\myrepo\\pythonlab\\myworkouts\\execute-config-steps.txt",'a+')

step = ''
i = 1
userInput = ''

while( userInput.lower() != 'q' ):
    userInput = input('step:')
    if(userInput.lower() == 'q'):
        step = '\n\nExpected:\nActual:\n'
        step = step + '\n\n##################################################################################'
        filePath.write(step)
        break
    else:
        step = str(i) + '.' + userInput + '\n'
        filePath.write(step)
        i= i+1

filePath.close()
    


