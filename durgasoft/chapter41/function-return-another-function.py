def outer():
    print('outer function')
    def inner():
        print('inner function')
    print('outer returning innner function...')

    def inner2():
        print('inner 2 function')
    return inner, inner2

f1,f2=outer()

f1()
f2()
