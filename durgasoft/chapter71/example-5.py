import re

pattern = input('enter pattern:')
text = input('enter text:')

matchedObject = re.search(pattern,text) # search it not iterable.

print(matchedObject.group())