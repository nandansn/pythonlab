#program to find the factorial of the number

number = int(input(
    "Enter the number to find the factorial"
))

factorial = 1
for i in range(1,number+1,1):
    factorial = factorial * i

print("factorial of {} is ".format(number),factorial)

