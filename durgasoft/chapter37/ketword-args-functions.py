'''
passing arguments, using the keyword.
order is not important
'''

def wish(name,msg):
    print ('Hello {} {}'.format(name,msg))

wish(name='nanda',msg='good morning')
wish(msg='good evening',name='kumar')
wish('kumar',msg='good evening')
#wish('kumar',name='kumar')  Argument 'name' passed by position and keyword in function
# wish(msg='good evening','gopal') SyntaxError: positional argument follows keyword argument
