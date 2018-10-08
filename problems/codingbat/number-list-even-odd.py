
numList = [2,3,6,8,1,4,7]

evens = list(filter(lambda n : n%2 ==0,numList))

odds = list(filter(lambda n: n%2 != 0,numList))

print(evens)

print(odds)