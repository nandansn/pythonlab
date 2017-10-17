def sum(a,b):
    c = a + b;
    return c

print(sum(10,11))


#pass by reference
def listops(mylist):
    mylist.append(10);


mylist = [1,3,2]

listops(mylist)

print(mylist)


#assigning new reference

def listbyvalue(list1):
    list1 = [1,2,3]

list1 = [10,11,12]
print(list1)

#keyword args

def subtract(a,b):
    return b -a

print(subtract(10, b =20))


# default args

def mul(a=10, b=20):
    return a * b

print(mul())

# variable args

def add(*args):
    sum =0
    for num in args:
        sum = num + sum;

    return sum

print(add(1,2))
print(add(1,2,2))

#lambda

sum = lambda arg1,arg2: arg1 + arg2

print(sum(10,12))




