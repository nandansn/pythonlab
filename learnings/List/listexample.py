count = input("How many persons?")

names = []

for i in range(0,int(count)):
    name = input("Name:")
    names.append(name)


def displayNames(names=[]):
    for name in names:
        print(name)

print(displayNames(names))

# get using negative index

print(names[-1]) # prints the value from the reverse