# print all prime numbers in a interval

start = int(input("enter start of the interval"))
end = int(input("enter end of the interval"))

primeNumbers = []

for number in range(start,end,1):
    primeFlag = True
    for i in range(2,number,1):

        if primeFlag:

            remainder = number % i

        if remainder == 0:

            primeFlag = False

    if primeFlag:
        primeNumbers.append(number)

print("List of prime numbers between {} and {}".format(start,end),primeNumbers)
