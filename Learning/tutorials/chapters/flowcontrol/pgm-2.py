#program to check the entered number is odd or even

number = int(input("enter the number:"))

remainder = number % 2;

if remainder !=0:
    print("number {} is odd".format(number))

else:
    print("number {} is even".format(number))
