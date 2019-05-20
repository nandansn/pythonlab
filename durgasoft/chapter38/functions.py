'''
function: outside the class,
method: inside the class

var-length argument.
var-arg type is tuple.
'''

def add(*num):
    print(type(num))
    for i in num:
        print(i)

add(10,2,3,4,5)
add(10,'nanda',[1,4,5,'k',(1,2,'a')])


def display(*n,name):
    print(name)
    for i in n:
        print(i)

display(1,2,3,name='nanda')
# display(name='nanda',12,3,4) positional argument follows keyword argument

'variable keyword arguments **kwargs, Type of kwargs is dict'

def display2(**kwargs):
    print(type(kwargs))
    print(kwargs)

display2(name='nanda',age='39',org='oracle')
