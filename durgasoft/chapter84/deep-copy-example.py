import copy

l1 = [1,2,3,[7,8,9],4,5,6]
l2 = copy.deepcopy(l1)

print ('l1: ',l1)
print ('l2: ', l2)

l1[0] = 11
l2[0] = 110


l1[3][0] =17
l2[3][0] = 177

print (l1)
print (l2)
