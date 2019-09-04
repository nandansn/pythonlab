class G:
    def m1(self):
        print('grand parent')

class P(G):
    def m2(self):
        print('parent')

class C(P):
    def m3(self):
        print('grand child')

c = C()
c.m3()
c.m2()
c.m1()
