class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,other):
        m1Total =  self.m1 + other.m1
        m2Total = self.m2 + other.m2
        return m1Total, m2Total

st1 = Student(10,12)
st2 = Student(22,11)

print(st1 + st2)
