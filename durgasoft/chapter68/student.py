from person import Person

class Student(Person):
    def __init__(self,name,age,sex):
        super().__init__(name,age,sex)
        print('child')
        self.childname ='child'

    def child(self):
        print(self.__dict__)
        

s = Student("Nanda","39","40")
s.child()