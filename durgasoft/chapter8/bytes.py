''' bytes data type , it is like an array, this is immutable. to use mutable array use bytearray.'''

x = [10,20,30,40]

b = bytes(x)


for i in b: print(i)

# b[0]=50 immutable: Error: TypeError: 'bytes' object does not support item assignment


b = bytearray(x)
b[0]=50

for i in b: print(i)

b[0]=500 # ValueError: byte must be in range(0, 256) 



