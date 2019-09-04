'''
default argument.
    default argument, should be the last argument.
'''

def wish(name,msg='Have a nice day'):
    print('Hell, {} {}'.format(name,msg))

wish('Nanda')
wish('Nanda','Good Morning')

# def display(name='Guest',msg): default argument follows non-default argument
    #print('{} {}'.format(name,msg))

