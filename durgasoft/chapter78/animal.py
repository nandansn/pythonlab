from abc import *
class Animal(ABC):
    @abstractmethod
    def action(self):
        pass

    def eat(self):
        print('eating')

class Dog(Animal):
    def action(self):
        print('dog barks')

class Tiger(Animal): pass

d = Dog()
d.action()
d.eat()

# a = Animal() # TypeError: Can't instantiate abstract class Animal with abstract methods action
# a.action()

# t = Tiger() TypeError: Can't instantiate abstract class Tiger with abstract methods action