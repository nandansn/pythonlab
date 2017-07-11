class Employee:
    name="nanda"
    id="123"
    salary=10000000

    def printEmployee(self):
        print(self.id)
        print(self.name)
        print(self.salary)

    def getEmployeeSalary(self):
        return self.salary


employeeOne = Employee()
employeeOne.name = "kumar"
employeeOne.id = 124
employeeOne.printEmployee()

print(employeeOne.getEmployeeSalary())
