principal = 5000
time = 55
intr = 3.50

r = ((((principal * 3.50)/100)/12)/30)*7

print (r)

for i in range(275):
    r = ((((principal * 3.50)/100)/12)/30)*7
    principal = principal + r

print(principal)

