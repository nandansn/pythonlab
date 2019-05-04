from sys import argv

print(argv)

'''
output will be, ['.\\cmd-line-args.py', '10', '20', '30', '40']

first item in the list is file.

'''

print(argv[1:])

s=0

for i in argv[1:]:
    s= s + eval(i)

print(s)
