#Example use with map()
#The map() function in Python takes in a function and a list.

# The function is called with all the items in the list and a new list is returned which contains items returned by
# that function for each item.

numbers = [1,2,3,4,5]


new_numbers = list(map(lambda number: number * 2, numbers))

print(new_numbers)
