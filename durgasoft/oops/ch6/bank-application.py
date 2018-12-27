

class BankAccount:
    bankAccounts =[]
    accountNumberCounter = 1220180000
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.accountNumber = BankAccount.incrementAccountNumber()
        BankAccount.addBankAccount(self)
        print("Account created. Account Number is:"+str(self.accountNumber))
        
        

    def deposit(self,amount=0):
        self.balance = self.balance + amount
        print(self.accountNumber)
        print(self.balance)
    
    def withdraw(self, amount=0):
        if self.balance <= 0:
            print("No funds, you can't withdraw.")
            return 0
        if amount > self.balance:
            print("Insufficient fund in the account.")
            return 0
        else:
            self.balance = self.balance - amount
            print("Amount withdrawn.\nAvailabe balance is:"+str(self.balance))
        

    @classmethod
    def incrementAccountNumber(cls):
        cls.accountNumberCounter = cls.accountNumberCounter + 1
        return cls.accountNumberCounter

    @classmethod
    def addBankAccount(cls,account):
        cls.bankAccounts.append(account)

    @staticmethod
    def checkIfAccountExist(acctNum,accounts):
        for account in accounts:
           if  account.accountNumber == acctNum:
               return account
        

print(""" Account Operation
          1. Create Account
          2. Deposit 
          3. Withdraw
          4. Exit""")


option = int(input("Enter Option:"))
while True:
    if option < 1 or option > 4:
        print("invalid option")
        print(""" Account Operation
          1. Create Account
          2. Deposit 
          3. Withdraw
          4. Exit""")
        option = int(input("Enter valid option(1 to 4):"))
    else:
        break
    
while (option != 4):
    if option == 1:
        name = input("Enter Name:")

        amount = int(input("Enter amount:"))
        BankAccount(name,amount)
        option = int(input("Enter Option:"))

    if option == 2:
        accountNumber = int(input("Enter Account Number:"))
        amount = int(input("Enter Amount:"))
        BankAccount.checkIfAccountExist(accountNumber,BankAccount.bankAccounts).deposit(amount)
        option = int(input("Enter Option:"))
    if option == 3:
        accountNumber = int(input("Enter Account Number:"))
        amount = int(input("Enter Amount:"))
        BankAccount.checkIfAccountExist(accountNumber,BankAccount.bankAccounts).withdraw(amount)
        option = int(input("Enter Option:"))
        





