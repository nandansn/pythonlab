class P:
    def m1(self):
        print('Parent..')

class C1(P):
    def m2(self):
        print('Child 1...')

class C2(P):
    def m3(self):
        print('Child 2...')

c1 = C1()
c1.m1()
c1.m2()

c2 = C2()
c2.m1()
c2.m3()