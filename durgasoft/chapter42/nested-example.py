def outer():
    def display():
        print('inner')
    
    display()
    print('do some thing')
    display()
    print('do anything')
    display()

outer()