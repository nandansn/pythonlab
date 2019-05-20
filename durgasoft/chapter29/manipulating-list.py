'list manipulating methods...'

'adding element'

ls = []

ls.append(1)
ls.append(2)
ls.append(2)

print(ls)

'insert - added element at particular position. costly if u try to add the element in the middle of the list.'



ls.insert(2,4)

print(ls)


'extend method to add all the elements from another list'

ls.extend([90,78,56])
print(ls)

' using + operator we can extend the elements, we need to assign the value to list object here '
ls=ls + [3,4,5,6]

print(ls)