class Customer():
    ''' document string : we can describe about this class '''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def pirntCustomerDetails(self):
        print(self.name)
        print(self.age)
        print(Customer.__doc__)


