

def fib():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b

fibvalues=fib()

for i in fibvalues:
    if i > 100:
        break
    else:
        print(i)