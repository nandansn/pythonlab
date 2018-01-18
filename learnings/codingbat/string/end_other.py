def end_other(a="",b=""):
    a = a.lower()
    b = b.lower()

    if (len(a) > len(b)):
        return a.endswith(b)
        
    else:
        return b.endswith(a)


print(end_other('abc', 'abc'))
        