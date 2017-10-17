# to check the number is armstrong or not

number = input("enter the number:")

length = len(number)

armstrong = 0

print("length is ",length)

tempNumber = int(number)

while tempNumber > 0:
    remainder = tempNumber % 10;
    i =0
    t = 1
    while i < length:
        t = t * remainder;
        i = i +1
    armstrong = t + armstrong
    print(armstrong)
    tempNumber = int(tempNumber / 10);

if armstrong == int(number):
    print("{} is armstrong".format(number))
else:
    print("{} is not armstrong".format(number))







