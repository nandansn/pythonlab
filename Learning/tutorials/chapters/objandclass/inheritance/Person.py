class Person:
    name =""
    age = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getPerson(self):
        return self

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

