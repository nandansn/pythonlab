''' Pattern:
12345
1234
123
12
1
'''

maxNumber = int(eval(input("enter the number:")))
num = 1
printNum=''
maxNumber = maxNumber+1
jmaxNumber = maxNumber
for i in range(1,maxNumber):
    printNum=''
    
    for num in range(1,jmaxNumber):
        printNum = printNum + str(num)
    print(printNum)
    jmaxNumber = maxNumber-i
    
    

