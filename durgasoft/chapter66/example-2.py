class Car:
    def outerClassCar(self):
        print('car outer class method')
    def startCar(self):
        self.e = Car.Engine()
        self.e.startEngine()
        print('car started...')
    class Engine:
        def innerClassEngine(self):
            print('engine inner class method')

        def startEngine(self):
            print('engine started...')

c = Car()
e = Car().Engine()

c.outerClassCar()
e.innerClassEngine()

c.startCar()