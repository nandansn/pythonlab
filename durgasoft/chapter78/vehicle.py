from abc import abstractmethod
class Vehicle:
    @abstractmethod
    def getwheels(self):
        pass

class Cycle(Vehicle):
    def getWheels(self):
        return 2

class Car(Vehicle):
    def getwheels(self):
        pass


c = Cycle()
print(c.getWheels())

v = Vehicle()