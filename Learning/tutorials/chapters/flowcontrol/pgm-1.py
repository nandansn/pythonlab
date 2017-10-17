# program to check the entered number is positive, negative or zero.

number = int(input("what is the number?"))

if number < 0:
    print("number {} is negative".format(number))

elif number > 0:
    print("number {} is positive".format(number))
else:
    print("number {} you entered is zero".format(number))
