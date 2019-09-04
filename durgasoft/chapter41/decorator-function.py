'''
decorator function take function as input.
used to extend the functionality of the existing function, without modifying the existing function.
makes our code shorter.
decorator chainin, output of one decor to another decor, in multiple decor flow from top to bottom,

in below example,
input to decor_fun is decor_fun2, input to decor_fun2 is fun_one
'''



def decor_fun(func):
    def inner():
        print('decor inner')
        func()
    return inner

def decor_fun2(func):
    def inner():
        print('decor outer')
        func()
    return inner


    

@decor_fun 
@decor_fun2
def fun_one():
    print('hiiii')


fun_one()