class Person:
    def __init__(self,name,age,phone):
        self.name = name
        self.age = age
        self.phone = phone

    def display(self):
        print(self.__dict__)

    def del_name(self):
        del self.name

p = Person('Nanda',32,2345678)
p.display()
p.del_name()
p.display()
del p.phone
p.display()