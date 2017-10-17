# size of the list can be updated. we can add, remove, update, insert elements.

week_days = ['monday','tuesday','wednessday','thursday','friday']


week_ends= ['saturday','sunday']

print(week_days)

print(week_ends)

print('all days of week')
print( week_days + week_ends)

print('mid of the week')
print(week_days[2:week_days.__len__()-1])

print('number of working days')
print(week_days.__len__())

#adding new element at the end
week_days.append('nanda')
print(week_days)

#inserting new element
week_days.insert(1,'kumar')
print(week_days)


#remove element
week_days.remove('kumar')
week_days.remove('nanda')

print(week_days)





