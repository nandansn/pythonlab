# In Python, function is a group of related statements that perform a specific task.

# Functions help break our program into smaller and modular chunks.
# As our program grows larger and larger, functions make it more organized and manageable.

# Keyword def marks the start of function header.
# A function name to uniquely identify it. Function naming follows the same rules of writing identifiers in Python.
# Parameters (arguments) through which we pass values to a function. They are optional.
# A colon (:) to mark the end of function header.
# Optional documentation string (docstring) to describe what the function does.
# One or more valid python statements that make up the function body. Statements must have same indentation level (usually 4 spaces).
# An optional return statement to return a value from the function.

def display():
    """
        this is the function which displays
    :return:
    """
    print("display function")

def displayOne(names):
    print(names)

display()
print(display.__doc__)
displayOne(['nanda','kumar','nivithi'])


