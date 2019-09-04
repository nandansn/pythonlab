import os

if os.path.isfile('log1.txt') :
    print('file found')
else:
    print('file not found')

f=open('log.txt','r')

print(f.read())

for data in f.readline(10):
    print(data)

f.close()

with open('log.txt','r+') as f:
    print(f.read())
    print(f.write('nanda')) # write method returns number of cahrs written.
    print(f.tell())


with open('offset.txt','r') as f2:
    print(f2.seek(-2,2))
    print(f2.read())