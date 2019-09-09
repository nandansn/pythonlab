def myGen():
    yield 'A'
    yield 'B'
    yield 'C'

g = myGen()

#print(next(g))
print(next(g))
#print(next(g))


for x in g:
    print('loop:',x)