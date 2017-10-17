#assignments

integer = 10;
realnumber = 12.5;
nameString = "nanda"

# multiple assignments

a= b= c = 10;

print(a,b,c)

a,b,c = 10, 10.5, "kumar"

print(a,b,c)

#data types
#python numbers

number = 12;

print(type(number))

number = 12.5
print(type(number))

name = "karthi"
print(type(name))

#list
    #Lists are mutable, meaning, value of elements of a list can be altered.
    #We can use the slicing operator [ ] to extract an item or a range of items from a list.
    # Index starts form 0 in Python.
    #All the items in a list do not need to be of the same type


carlist = ['alto','city','bmw','audi']

print(carlist[0])
print(carlist[2:3])
carlist[3]='rolls royce'
carlist.append('baleno')
print(carlist[3:])


#Tuples
    #Tuple is an ordered sequence of items same as list.
    # The only difference is that tuples are immutable. Tuples once created cannot be modified.


mytuple =(5,2,'nanda',12.5)

print(mytuple[0:])


# String
    #String is sequence of Unicode characters. We can use single quotes or double quotes to represent strings.
    # Multi-line strings can be denoted using triple quotes, ''' or """.
    # Strings are immutable in Python

country = "India"

state = '''Tamil nadu
            Andhra'''

print(country)

print(state)

print(state.__len__())

# Set
    # Set is an unordered collection of unique items. Set is defined by values separated by comma inside braces { }.
    # Items in a set are not ordered.
    #We can perform set operations like union, intersection on two sets.
    # Set have unique values. They eliminate duplicates.
    #Since, set are unordered collection, indexing has no meaning.
    # Hence the slicing operator [] does not work.

sarees ={'kalamkari','kalamkari','Kalamkari'}

print(sarees)

# Dictionary
    # Dictionary is an unordered collection of key-value pairs.
    # It is generally used when we have a huge amount of data. Dictionaries are optimized for retrieving data.
    # We must know the key to retrieve the value
    # In Python, dictionaries are defined within braces {} with each item being a pair in the form key:value
    # Key and value can be of any type.

students={1:'nanda',2:'kumar',3:'karthi',4:'deepak'}

print(students.keys())

print(students.values())

# conversion between data types

print(int(10.5))
print(float(12))
print(int('11'))
print(float('12.3'))
print(int('nanda')) # nothing will happen
print(int('11.2')) # nothing will happen

# converting one sequence to another

print(set([1,2,3]))
print(list('hello'))
print(dict([1,2],[3,4]))
