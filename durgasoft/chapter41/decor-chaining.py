def double_decor(funct):
    def inner():
        x=funct()*2
        return x

    return inner


def square_decor(funct):
    def inner():
        num=funct()
        x=num*num
        return x
    return inner

def result(funct):
    def inner():
        print(funct())
    return inner

@result
@square_decor
@double_decor
def getnum():
    return int(input('enter number:'))


getnum()