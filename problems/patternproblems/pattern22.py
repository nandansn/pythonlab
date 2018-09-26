number = int(input('Enter Number:'))

asciiCodeOfA = ord('A')

endNumber = asciiCodeOfA + number -1
count = number
for i in range(endNumber, asciiCodeOfA -1, -1):
    print(chr(i)*count)
    count = count - 1



