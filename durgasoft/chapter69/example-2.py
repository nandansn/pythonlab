class P:
    a=10
    def __init__(self):
        self.b=20

class C(P):
    a=15
    def __init__(self):
        super().__init__()
        self.b=30
        print(super().a)
        print(self.a)
        print(self.b)

c = C()