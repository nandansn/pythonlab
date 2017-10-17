# program to check the entered year is leap year or not

year = int(input("Enter the year:"))

leap = year % 4;

if leap:
    print("{} is not leap year".format(year))
else:
    print("{} is leap year".format(year))
