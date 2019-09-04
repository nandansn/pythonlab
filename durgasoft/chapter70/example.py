import re

pattern = input('enter pattern:')
sentence = input('enter sentence:')

matcher = re.finditer(pattern,sentence)

for match in matcher:
    print('matched string: {}'.format(match.group()))