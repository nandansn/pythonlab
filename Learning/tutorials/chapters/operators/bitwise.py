# Bitwise operators act on operands as if they were string of binary digits. It operates bit by bit, hence the name.

x = input("enter number x:")
y = input("enter number y:")

x = int(x)
y = int(y)

print("bitwise {} and {}".format(x,y), x & y)

print("bitwise {} or {}".format(x,y), x | y)

print("bitwise not of {} ".format(x), ~x)

print("bitwise {} xor {}".format(x,y), x ^ y)

print("bitwise right shift".format(x), x >> 2)

print("bitwise left shift".format(x), x << 2)
