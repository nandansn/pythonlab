''' for loop '''

name = input('enter name:')

for c in name:
    print('{0}\n'.format(c))

names = [name for name in input('enter names:').split(',')]

for name in names:
    print('name:{0}'.format(name))

for i in range(10):
    print('number:{0}',format(i))
evens =[]
odds=[]
primes=[]
j=1
for i in range(1,5000):
    if (i%2==0):
        evens.append(i)
    else:
        for k in range(1,i+1):
            if i in primes:
                break
            elif (i==1):
                primes.append(i)
                break
            elif (i == k):
                primes.append(i)
            elif (i%k==0 and k !=1):
                break
           
            
        odds.append(i)
print(evens)
print(odds)
print(primes)