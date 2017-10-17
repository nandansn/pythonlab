# break and continue

# In Python, break and continue statements can alter the flow of a normal loop.

# Loops iterate over a block of code until test expression is false, but sometimes we wish to terminate the current
# iteration or even the whole loop without cheking test expression.

# The break and continue statements are used in these cases.

number = int(input("enter number:"))

i = 0

while i < number:
    i+=1
    if i == 10:
        breakNumber = bool(input("enter break number:"))

        if breakNumber:
            break
        else:
            continue
    else:
        print(i)



