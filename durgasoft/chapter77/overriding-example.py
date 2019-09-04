class Parent:
    def Marry(self):
        print('arranged marriage')

    def Property(self):
        print('Parent property')

class Child(Parent):
    def Marry(self):
        print('love marriage')

    def arranged(self):
        super().Marry()


c1 = Child()

c1.Property()
c1.Marry()

c2 = Child()
c2.arranged()