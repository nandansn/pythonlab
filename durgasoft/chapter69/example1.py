class P:
    a=10
    def m1(self):
        self.a=20
       

class C(P):
    def m2(self):
        print(super().a)
        super().m1() # self.m1()
        print(self.a)

c = C()
c.m2()