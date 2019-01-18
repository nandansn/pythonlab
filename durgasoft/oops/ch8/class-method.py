class Student:
    collegeName ="NSN University"

    @classmethod
    def classMethod(cls):
        print(cls.collegeName)

    def instanceMethod(self):
        print("Using self:"+self.collegeName)
        print("Using class name:"+Student.collegeName)

    @classmethod
    def classMethodTwo(cls,name):
        print("Student {0} is studying in {1} ".format(name,cls.collegeName))

    @classmethod
    def classMethodThree(clstwo):
        print(clstwo.collegeName)

Student.classMethod()
Student().instanceMethod()
Student.classMethodTwo('nanda')
Student.classMethodThree()