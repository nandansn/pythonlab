class Employee(object):
    name=""
    salary=0.0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def getName(self):
        return self.name

    def printEmployee(self):
        print("Employee => {Name:+"+self.getName()+",Salary:"+str(self.salary)+"}")

