class Duck:
    def talk(self):
        print('quack')

class Cat:
    def talk(self):
        print('meow')

class Goat:
    def talk(self):
        print('myaaah')

class Dog:
    def walk(self):
        print('walking')

l=[Duck(),Cat(),Goat(),Dog()]

for obj in l:
    if (hasattr(obj, 'talk')):
        obj.talk()
    else:
        print('''this object {0} don't have talk'''.format(type(obj)))