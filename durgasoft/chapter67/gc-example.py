class Student:
    def __init__(self):
        print('constructor....')
    
    def __del__(self):
        print('destructor....')

s = Student()
t=s
s=None
print('after none..')
del t
