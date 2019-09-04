from random import *

def otp():
    return randint(100000,999999)

n=0
list=[]
while True:
    n=otp()
    if n not in list: 
        print(n)
        list.append(n)
    else:
        break
print(len(list))
    


    