name =''
name = input('enter name:')
search = input('seacrh:')

try:
    print('index of {} in {} is {}'.format(search,name,name.index(search)))
except ValueError:
    print('string {} not found in {}'.format(search,name))
    