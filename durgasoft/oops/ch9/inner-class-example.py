class Car:
    def __init__(self,color,price):
        self.color=color
        self.price=price
        print('car created')

    def displayCar(self):
        print(self.__dict__)

    class Engine:
        def __init__(self,cc,version):
            self.cc=cc
            self.version=version
            print('engine created')

        def displayEngine(self):
            print(self.__dict__)

car = Car('blue',1234567)
carEngine = car.Engine(1400,'petrol')

