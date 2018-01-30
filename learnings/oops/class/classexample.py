class Account(object):
    accountNumber = 0
    balance = 0
    accountName =""

    def __init__(self,accountName,accountNumber,balance):
        self.accountName = accountName
        self.accountNumber= accountNumber
        self.balance = balance


x = Account("Nandakumar",1234567,5000000)

print(x.accountNumber)
print(x.accountName)
print(x.balance)