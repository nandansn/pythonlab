class Student:
    sname='CS Academy'
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(self.__dict__)

s = Student('Nivrithi','8')
s.display()
print(s.sname)
print(Student.sname)