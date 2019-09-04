import re

pattern = input('enter pattern:')
text = input('enter test:')

listObjs = re.split(pattern,text)

print(listObjs)