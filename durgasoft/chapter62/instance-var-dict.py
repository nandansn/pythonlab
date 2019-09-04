class Student:
    def __init__(self,name,rno,marks):
        self.name= name
        self.rno= rno
        self.marks = marks

    def display(self):
        print('Name:',self.name)
        print('Rollno:',self.rno)
        print('Marks:',self.marks)


s1 = Student('ABC',10,{'eng':90,'tam':100})

s1.display()

print(s1.__dict__)