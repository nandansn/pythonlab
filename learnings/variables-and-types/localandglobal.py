x = 10 # gloabl scope

def display():
    y = 20 #local scope
    print(x)

display()

# print(y) # out of scope

if __name__ == "__main__":
    name ={"server":"tomcat",\
    "db":"oracle"

    } # global scope



print(name)

# n # Referencing an Unbound Variable


# assigning multiple values at once

v = (1,2,3,4)

(a,b,c,d) = v

print(v)

print(a,b,c,d)

v =[5,6,7]

(a,b,c) = v

print(a,b,c)

# assigning range of values
# 	The built-in range function returns a list of integers. 
#   In its simplest form, it takes an upper limit and returns a zero-based list counting up to but not including the upper limit. (If you like, you can pass other parameters to specify a base other than 0 and a step other than 1.

(a,b,c,d) = range(0,8,2)

print(a,b,c,d)

print(range.__doc__)

print(d)

# return range of values
def getRangeOfValues():
    return (1,2,3,4)

(a,b,c,d) = getRangeOfValues()

print(a,c,d,b)
