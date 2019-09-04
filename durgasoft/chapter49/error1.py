try:
    print(10/0)
except ZeroDivisionError as error1:
    print(error1.__doc__)
