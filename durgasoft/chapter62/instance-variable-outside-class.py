class Stock:
    def __init__(self,name,cmp):
        self.name=name
        self.cmp=cmp

    def low(self,todayLow):
        self.todayLow = todayLow

    

s = Stock('GAIL',145)
print(s.__dict__)
s.low(140)
print(s.__dict__)
s.high = 200
print(s.__dict__)