class Father:
    def m1(self):
        print('height is 6 feet')

class Mother:
    def m1(self):
        print('color is brown')

class Child(Father, Mother):
    def m1(self):
        super().m1()



c = Child()
c.m1()
