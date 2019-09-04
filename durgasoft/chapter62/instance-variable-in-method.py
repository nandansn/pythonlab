class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def empAge(self,age):
        self.age=age

e1 = Employee('Nanda','1000000000000')

print(e1.__dict__)

e1.empAge(39)

print(e1.__dict__)