import re

pattern = '[6|8|9][0-9]{2}'
patternToObject = re.compile(pattern) 

print(type(patternToObject))

matcherObject = patternToObject.finditer('900 700 800 python is easy to learn. Love to learn python')

for match in matcherObject:
    print('start index of the match is:{}'.format(match.start()))
    print('end index of the match is:{}'.format(match.end()))
    print(match.group())