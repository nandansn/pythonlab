class Car:
    def __init__(self, name,brand,price):
        self.name = name
        self.brand = brand
        self.price = price

    def display(self):
        print(self.__dict__)

        