class Customer():
    ''' document string : we can describe about this class '''

    cname='nanda corp'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def pirntCustomerDetails(self):
        print(self.name)
        print(self.age)
        print(Customer.__doc__)

    @classmethod
    def compnayName(cls):
        print(cls.cname)

    @staticmethod
    def sum(a,b):
        print(a+b)
        


print(Customer.cname)
Customer.compnayName()
Customer.sum(10,11)