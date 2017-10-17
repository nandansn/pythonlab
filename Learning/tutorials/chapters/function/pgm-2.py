numbers = [1,2,3,4,5,6,7,8]

divisible_numbers = list(filter(lambda number: (number % 2) == 0 , numbers ))

print(divisible_numbers)
