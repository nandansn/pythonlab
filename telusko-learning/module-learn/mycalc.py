from functools import reduce

def mysum(*varArgs):
    return reduce(lambda x,y : x + y,varArgs)