class Employee():
    
    companyName='Oracle'

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def displayEmp(self):
        print("Name: {0} Age {1}".format(self.name,self.age))
        print(Employee.companyName)
    
    @classmethod
    def displayOrgName(cls):
        print(Employee.companyName)

        print(cls.companyName)
    
    @staticmethod
    def calculateSal(basic,hra,spl):
        print(hra+basic+spl)




emp1 = Employee('nanda',38)

emp1.displayEmp()
emp1.displayOrgName()

emp1.calculateSal(10,12,30)