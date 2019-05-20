'''
mathematical operations,
union,
intersection,
difference,
symmetric difference, element present in s1 and not in s2, element present in s2 and not in s1


'''

s1=set()
s2=set()

s1.update([1,2,3,4])
s2.update([5,6,7,8,1])

s3=s1.union(s2)

print(s3)

s4=s1.intersection(s2)

print(s4)

s5=s1.difference(s2)

print(s5)

s6=s1.symmetric_difference(s2)

print(s6)