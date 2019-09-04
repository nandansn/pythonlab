class Employee:
    def __init__(self, name, perDayWage):
        self.name = name
        self.perDayWage = perDayWage

    def __mul__(self, timesheet):
        return self.perDayWage * timesheet.daysWorked


class TimeSheet:
    def __init__(self, daysWorked):
        self.daysWorked = daysWorked

e = Employee("Kumar",10000)
t = TimeSheet(30)

print('This month salary:{0}'.format(e*t)) 