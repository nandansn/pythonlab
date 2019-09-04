import re

pattern = input('enter pattern:')
text = input('enter text:')
replacetext = input('replace by:')

subObject = re.sub(pattern,replacetext,text)

print(subObject)