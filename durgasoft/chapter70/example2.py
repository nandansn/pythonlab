import re


# mail pattern = [a-z0-9]{13}[@][a-z]{5}[\.][a-z]{3}
pattern = input('enter pattern:')
text = input('enter text:')

matcher = re.finditer(pattern,text)

for match in matcher:
    print(match.group())