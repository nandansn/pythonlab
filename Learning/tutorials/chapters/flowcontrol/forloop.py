# The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects.
# Iterating over a sequence is called traversal.

names = ['nanda','dinesh','gnana','thiaghu']

for name in names:
    print(name)
else:
    print("no items left")

# The range() function. We can generate a sequence of numbers using range() function.
# range(10) will generate numbers from 0 to 9 (10 numbers).

for i in range(10):
    print(i)

mycars = ['BMW','Tesla','Audi','Porsche','Fortunner','Range Rover']

for car in range(len(mycars)):
    print(mycars[car])

# range: We can also define the start, stop and step size as range(start,stop,step size).

for i in range(10,21,2):
    print(i)
