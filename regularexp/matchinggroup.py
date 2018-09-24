import re

inputString = input('Enter the input text:')

pattern = '^<[\w]+>'

matched=re.search(r''+pattern,inputString)

print (matched)

if matched:
    print(matched.group())



