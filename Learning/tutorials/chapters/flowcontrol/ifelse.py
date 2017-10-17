# The if…elif…else statement is used in Python for decision making.

age = int(input("What is the age?"))

if age > 0:
    if age <= 4:
        print("stay at home and have fun")
    elif age > 4 and age < 6:
        print("go to kinder garden")
    elif age >= 6 and age <= 18:
        print("go to school")
    elif age >= 19 and age <=22:
        print("go to college")
    else:
        print("go to job")
else:
    print("age you have entered is invalid")

