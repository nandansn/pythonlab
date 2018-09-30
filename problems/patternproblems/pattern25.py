maxNumber = int(input('Enter Number:'))

count = 1
prev =''
for i in range(maxNumber, 0, -1):
    printPattern = (' ' * i)
    print(printPattern + prev + str(count))
    prev = prev + str(count)
    count += 1
