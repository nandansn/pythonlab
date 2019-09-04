class P:
    def __init__(self):
        self.b = 10

class C(P):
    def __init__(self):
        self.b=20
        super().__init__()
        print(self.b) # parent class b value, only one copy, lateest initialized copy.


c = C()
