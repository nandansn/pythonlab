class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.__dict__)

class Test:
    @staticmethod
    def testEmp(employee):
        employee.display()

    
t = Test()
e = Employee('Nanda',1200000000)
Test.testEmp(e)


    
