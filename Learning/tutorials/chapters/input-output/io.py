#input
# input([prompt]). where prompt is the string we wish to display on the screen. It is optional.

name = input("Enter the name:")

print(name)


#output formatting

print("my name is {}".format(name))

real = input("enter any real number:")

print("entered real number is %2.3f"  %float(real))
