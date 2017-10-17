# all reference and assignment are to the global a due to the use of keyword global.

a = 20

def outer_function():
    global a
    a = 30

    def inner_function():
        global a
        a = 40

        print(a)
    inner_function()
    print(a)

outer_function()
print(a)
