import sys

class Student:
    def __init__(self):
        print("student registered")


s = Student()

r1 = s
r2 = s
r3 = s

print(sys.getrefcount(s)) # pyhton will create one internal reference