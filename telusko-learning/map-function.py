'''
One of the common things we do with list and other sequences is applying an operation
 to each item and collect the result.

'''

numList = eval(input('Enter numbers:'))

results =list(map(lambda n: n * 2, numList))

print(results)
