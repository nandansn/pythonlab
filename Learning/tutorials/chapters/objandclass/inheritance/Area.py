class Area:
    def __init__(self, a, b):
        self.side_1 = a;
        self.side_2 = b;

    def cal_area(self):
        self.area = self.side_1 + self.side_2


class Square(Area):
    def __init__(self, s1):
        self.side = s1
        Area.__init__(self,self.side,self.side)

    def cal_area(self):
        print("square: ",self.side_1 * self.side_2)


obj = Square(10);

obj.cal_area()
