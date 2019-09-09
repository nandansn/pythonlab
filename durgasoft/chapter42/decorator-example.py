def decorateWish(func):
    def inner(name):
        if name == 'Nanda':
            print('good morning boss')
        else:
            func(name)
    return inner


@decorateWish
def wish(name):
    print('good morning {0}'.format(name))

def wishWithoutDecorAnnotation(name):
    print('good morning {0}'.format(name))

decorCalling = decorateWish(wishWithoutDecorAnnotation)

decorCalling('nanda')


wish('raju')
wish('Nanda')