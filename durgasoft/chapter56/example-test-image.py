import os

f1 = open('ppt.jpg','br')
bytes= f1.read()

f2 = open('new-ppt.jpg','bw')
f2.write(bytes)