class D: pass
class E: pass
class F: pass

class B(D,E): pass
class C(D,F): pass
class A(B,C): 
    @staticmethod
    def checkMRO():
        print(A.mro())

A.checkMRO()
