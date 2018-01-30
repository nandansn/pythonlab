class Account(object):
    # private 
    __name=""
    __balance=0.0

    def __init__(self):
        self
            
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setBalance(self, balance):
        self.__balance = balance

    def getBalance(self):
        return self.__balance

    
    def printAccountDetails(self):
        # string formatting example
        print("Account Name:{0},Account Balance:{1}".format(self.getName(),self.getBalance()))


