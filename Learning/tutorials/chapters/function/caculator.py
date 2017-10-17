def sum(*numbers):
    s = 0;
    for number in numbers:
        s = s + number
    return s

def sub(*numbers):
    s = 0;
    for number in numbers:
        s = s - number
    return s

def mul(*numbers):
    m = 1;
    for number in numbers:
        m = m * number
    return m

print(sum(1,2,3,4))
print(sub(2,3,4,5))
print(mul(1,2,3))
