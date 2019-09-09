def outer():
    def inner():
        print('inner function')
    return inner


f1 = outer()

f1()