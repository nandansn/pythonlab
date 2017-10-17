# Recursion is the process of defining something in terms of itself.

# example

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x -1))

x = int(input("enter the number:"))
print(factorial(x))

# Advantages of recursion
# Recursive functions make the code look clean and elegant.
# A complex task can be broken down into simpler sub-problems using recursion.
# Sequence generation is easier with recursion than using some nested iteration.
# Disadvantages of recursion
# Sometimes the logic behind recursion is hard to follow through.
# Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
# Recursive functions are hard to debug.

