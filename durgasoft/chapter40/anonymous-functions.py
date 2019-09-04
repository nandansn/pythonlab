'''
nameless functions
instant use only
lambda function: concise code.

syntax lambda input: expression
'''

s = lambda n: n*n

print(s(4))


k = lambda a,b : a if a > b else b


print("biggest of {} and {} is {}".format(10,20,k(10,20)))