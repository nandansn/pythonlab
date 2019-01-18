class Calculator:
    @staticmethod
    def add(x,y):
        print("sum is {}".format(x+y))

    @staticmethod
    def average(*x):
        average =sum(x)/len(x)
        print("average is {}".format(average)) 

Calculator.average(10,20,30)


        
