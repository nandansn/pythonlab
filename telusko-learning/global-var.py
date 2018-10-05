a = 10
print(a)
def test_global():
    
    a = 'local'
    x =globals()['a']

    
    
    print(x)

    print(a)

    globals()['a'] = 40

test_global()

print(a)