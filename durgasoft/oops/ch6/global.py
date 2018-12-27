x=0
y=0
z=0

class Global:
    def m1(self):
        global x
        x = 10

    @classmethod
    def m2(cls):
        global y
        y = 20
        print(x)

    @staticmethod
    def m3():
        global z
        z = 30
Global.m2()