import copy

l1 = [1,2,3,[7,8,9],4,5,6] # reference created for [7,8,9]

l2 = copy.copy(l1)

print('l1:', l1)
print('l2: ', l2)

l2[3][2] = 100

print('l1:', l1)
print('l2: ', l2)

l2[0] = 20

print('l1:', l1)
print('l2: ', l2)
