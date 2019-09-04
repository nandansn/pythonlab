class Test:
    def m1(self):
        print('no-arg method')

    def m1(self, b):
        print('one arg method')

    def m1(self, c, d):
        print('two arg method')

t = Test()
t.m1()