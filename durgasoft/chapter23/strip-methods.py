'''
strip() - to remove the spaces at the begining and end of the string.
lstrip() - to remove the spaces at end of the string.
rstrip() - to remove the spaces at the begining of the string

'''
name=''
name = input('enter name with spaces:')
print(name.strip())
lname = input('space at end:')
print(lname.lstrip())
rname = input('space at begining:')
print(rname.rstrip())