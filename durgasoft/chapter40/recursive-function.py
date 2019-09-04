def rec(n):
    f=1
    if (n == 1):
        return 1
    else:
        f=n*rec(n-1)
    return f


num=input('Enter number:')
num=int(num)
print(rec(num))
