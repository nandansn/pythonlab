class Customer:
    def __init__(self,name):
        self.name = name

    def display(self):
        def printName(self):
            print(self.name)
        
        printName(self)

    def closure_function_example(self):
        def closureFunction():
            print("closure function")
        
        return closureFunction

c=Customer('nanda')
c.display()

k = c.closure_function_example()

k()



