def add(a,b):
    return a+b


def validate(func):
    def inner(a,b):
        if a < b:
            print('a is less than b, so result will be negative')
            x=func(a,b)
            return x
        else:
            x=func(a,b)
            return x
    return inner
        


@validate
def sub(a,b):
    print(a-b)

