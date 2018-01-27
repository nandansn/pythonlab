def lone_sum(a,b,c):
    if a == b and a == c:
        return 0
    elif a != b and b == c:
        return a
    elif if b != c and a == c:
        return b
    elif if c != a and b == a:
        return c
    else:
        return a + b + c    