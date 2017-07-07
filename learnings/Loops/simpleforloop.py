# For loops iterate over a given sequence
names = ["nanda", "nilesh", "ashtoush"]

for name in names:
    print(name)

for numbers in (1,2,3):
    print(numbers)


# For loops can iterate over a sequence of numbers using the "range" and "xrange" functions.
# The difference between range and xrange is that the range function returns a new list with numbers of that specified range,
# whereas xrange returns an iterator, which is more efficient. (Python 3 uses the range function, which acts like xrange).
# Note that the range function is zero based.

for number in range(10,20):
    print(number)

#range and xrange takes 3 param, start,stop and step.
#start initial value, stop final value and step is increment and decrement.

for number in range(1,20,2):
    print(number)
