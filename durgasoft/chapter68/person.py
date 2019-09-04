class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        print('parent')

    def display(self):
        print(self.name)