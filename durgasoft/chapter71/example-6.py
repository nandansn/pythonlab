import re

text = input('Enter text to search and match:')
pattern = input('Enter pattern:')

matchers = re.findall(pattern,text)

print(matchers)