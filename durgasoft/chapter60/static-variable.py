'''
single copy for all the object. for example, company name is same for all the employees working in that company

one copy for all the objects,
can be accessed using class name or instance name,recommended is class name

'''

class Employee:
    companyName = 'Oracle'


e = Employee()

print(e.companyName)

print(Employee.companyName)

e2 = Employee()
e2.companyName = 'Apple' # instance variable companeName created for the instance e2. this wont affect the class variable companyName

print(e.companyName)