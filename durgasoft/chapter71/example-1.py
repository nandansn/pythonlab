import re

pattern = input('enter pattern:')
text = input('enter text:')

matcher = re.findall(pattern,text)

print(matcher)