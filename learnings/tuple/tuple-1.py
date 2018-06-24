months =('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec')

print('months:',months)

if ('jan' in months):
    print('jan exist')

if('jon' not in months):
    print('jon not exist')



#iterate
for name in months:
    print(name)

#slicing
for name in months[3:5]:
    print(name)

userInput = input("enter vale:")

if userInput in months:
    print('user input ',userInput,' exist' )
else:
    print('user input ',userInput,' not exist')
