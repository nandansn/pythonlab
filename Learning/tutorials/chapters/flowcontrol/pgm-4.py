#program to check the given number is prime number or not

number = int(input("enter the number"))

flag = True

for i in range(2,number,1):
    if flag:
        print(i)
        primeNumber = number % i
        print(primeNumber)

    if primeNumber:
        flag = True
    else:
        flag = False


if flag:
    print("{} is prime".format(number))
else:
    print("{} is not prime".format(number))
