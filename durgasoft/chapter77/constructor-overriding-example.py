class P:
    def __init__(self):
        print('parent class constructor')


class C(P):
    def __init__(self):
        print('child class constructor')


c = C()