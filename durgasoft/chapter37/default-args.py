'''
default argument.
    default argument, should be the last argument.
'''

def wish(name,msg='Have a nice day'):
    print('Hell, {} {}'.format(name,msg))

wish('Nanda')
wish('Nanda','Good Morning')

# def display(name='Guest',msg): non-default argument follows default argument
    #print('{} {}'.format(name,msg))

