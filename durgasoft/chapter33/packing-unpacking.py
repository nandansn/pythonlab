' tuple packing and unpacking '

a=10
b=20
c=30
t=a,b,c

print(t)
print(id(t))

t=(70,80,90)
print(id(t))
d,e,f = t

print('d={},e={},f={}'.format(d,e,f))

t='nanda'
i,j,k,l,m=t
print(i,j,k,l,m) 
i,j,k,l,m,n=t #ValueError: not enough values to unpack (expected 6, got 5)