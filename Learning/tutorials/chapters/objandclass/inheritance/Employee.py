import tutorials.chapters.objandclass.inheritance.Person as P

class Employee(P.Person):
    orgName =""
    salary =""

    def __init__(self,name,age,orgName,salary):
        self.__init__(name,age)
        self.orgName = orgName
        self.salary = salary

    def getEmployee(self):
        return self

    def getOrgName(self):
        return self.orgName

    def getSalary(self):
        return self.salary
