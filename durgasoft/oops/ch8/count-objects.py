class Car:
    countCars=0

    def __init__(self):
        self.name ="nanda"
        Car.countCars = Car.countCars + 1

    @classmethod
    def getCarsCreated(cls):
        print("Number of cars created {}".format(cls.countCars))


n = int(input("cars to be created:"))

for i in range(0,n,1):
    Car()

Car.getCarsCreated()
    