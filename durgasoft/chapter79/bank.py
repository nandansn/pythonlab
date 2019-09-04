class BankAccount:
    def __init__(self,account_number,balance):
        self.__account_number =  account_number
        self.balance = balance

    def display(self):
        print(self.__account_number)


b = BankAccount('123456',120000)
print(b.balance)
b.display()
#print(b._BankAccount__account_number) indirectly accessing the private member