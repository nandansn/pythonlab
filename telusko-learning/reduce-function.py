from functools import reduce

numList = eval(input('enter num list:'))

newList = list(numList)
results = reduce(lambda x,y : x +y,numList)

print('sum of numbers in list {} is {}'.format(newList,results))