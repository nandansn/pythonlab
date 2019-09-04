class Employee:
    company = 'Oracle'
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    @classmethod
    def display(cls):
        return cls.company
    @staticmethod
    def calc(sal,hra,da):
        return sal+hra+da
        

e = Employee()
e.setName('nanda')
print(e.getName())
print(e.display())

print(Employee.calc(10000000,222222,3333))