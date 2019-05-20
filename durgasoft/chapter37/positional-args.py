'''
actual arguments are passed as per the actual argument position.
number and order of args, must be matched.
'''

def add(a,b,c):
    print(a+b+c)

add(1,2,3)
# add(1,2,3,4) TypeError: add() takes 3 positional arguments but 4 were given