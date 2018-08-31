print(""" This is about arithmetic operators like,
+, -, *, /, %, //(floor division operator), **(power operator)""")

print (" Example: ")
a = 10
b = 20
print (a," + ",b," is:",a+b)
print (a," - ",b," is:",a-b)
print (a," * ",b," is:",a*b)
print (a," / ",b," is:",a/b)# division always return the output as float value.
print (a," % ",b," is:",a%b)
print (a," // ",b," is:",a//b) # floor division returns the nearest floor value. both a and b are int, return int. otherwise float.
print(10.5,"//",2,"is:",10.5//2)

print (""" can we apply + to string? 
yes but the combination shud e like str + str, str + other data types are not allowed""")

print('nanda'+'kumar')

# print('nanda'+37) # not allowed. TypeError: must be str, not int

print("""can we apply * to string?
yes we can apply, but the combination should be str * int""")

print("nanda"*2)
# print("nanda"*2.8) # TypeError: can't multiply sequence by non-int of type 'float'

print('''can we apply +, -, *, /,  %, // to bool type?
yes we can apply. Internally True and False are represented as 1 and 0.
''')

print(True+True)
print(True+False)

print(True - True)

print(True * True)

# print(True / False) # ZeroDivisionError: division by zero

print(False / True)

print(True % True)

print(True // True)