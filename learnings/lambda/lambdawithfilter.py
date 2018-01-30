numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

even = filter(lambda n: n % 2 == 0,numbers)

odd = filter(lambda n: n % 2 == 1,numbers)

print(list(odd))
print(list(even))



