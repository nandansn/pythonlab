class P:
    def __init__(self, eno, age):
        self.eno = eno
        self.age = age

class C(P):
    def __init__(self, eno, age, salary):
        super().__init__(eno,age)
        self.salary = salary

    def display(self):
        print(self.eno)

c = C('213213213',39,100000000000000000)
c.display()



