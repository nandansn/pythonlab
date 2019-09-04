from car import Car

class Employee:
    def __init__(self,name,car):
        self.name = name
        self.car = car

    def display(self):
        print('Emp Name: {}'.format(self.name))
        self.car.display()



c= Car('X7','BMW','One crore')

e= Employee('Nanda',c)

e.display()


