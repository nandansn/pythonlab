# At any given moment, there are at least three nested scopes.

# Scope of the current function which has local names
# Scope of the module which has global names
# Outermost scope which has built-in names

a = 20

def outer_function():
    a = 30

    def inner_function():
        a = 40

        print(a)
    inner_function()
    print(a)

outer_function()
print(a)


