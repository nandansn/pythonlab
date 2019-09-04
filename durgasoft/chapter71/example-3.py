import re

pattern = input('enter pattern:')
text = input('enter text:')
replaceText = input('replace text:')

subTuple = re.subn(pattern,replaceText,text)

print(subTuple[0])
print(subTuple[1])