class EMP:
    def __init__(self, name, doj):
        self.name = name
        self.doj = doj
        print("Employee object constructed...")

    def displayDetails(self):
        print(self.name)
        print(self.doj)

    def compareObjects(self,empObj):
        if self.name == empObj.name:
            return True
        else:
            return False

nanda = EMP('Nanda','13/10/1980')
yuvaraj = EMP('Yuvaraj','14/01/1980')

nanda.displayDetails()
yuvaraj.displayDetails()

print(nanda.compareObjects(nanda))