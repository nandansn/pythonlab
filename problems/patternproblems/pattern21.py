maxNum = int(input("Enter max number:"))

totalNum =''
printMaxNum = 0
for i in range(maxNum,0, -1):
    totalNum = ''
    for j in range(maxNum,printMaxNum,-1):
        totalNum = totalNum + str(j)
    printMaxNum += 1
    print(totalNum)