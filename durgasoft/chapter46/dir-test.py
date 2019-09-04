import moduleone

x=10
y=20

def test():
    global x
    x=20
    z=0
    print('dir test')
    print(x)

test()
print(dir())
print(dir(moduleone))