print(""" we can use eval function to read data, when we use eval function no need to make type conversion""")

#a,b,c,d,e=eval([x for x in input("Enter data:").split()])

a = eval(input("enter a:"))
b = eval(input("enter b:"))
c = eval(input("enter c:"))
d = eval(input("enter d:"))
e = eval(input("enter e:"))


print("value:",a,"type:",type(a))
print("value:",b,"type:",type(b))
print("value:",c,"type:",type(c))
print("value:",d,"type:",type(d))
print("value:",e,"type:",type(e))


a,b,c,d,e=[eval(x) for x in input("Enter data:").split()]

print("value:",a,"type:",type(a))
print("value:",b,"type:",type(b))
print("value:",c,"type:",type(c))
print("value:",d,"type:",type(d))
print("value:",e,"type:",type(e))

