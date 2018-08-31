numbers = '11111'

for i in range(1,6):
    k = int(numbers) * i
    print(k)
    numbers = numbers[0:5-i]