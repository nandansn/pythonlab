import re

myString ="nandakumar"



matchedPattern = re.findall(r'a|n|d|k|u|m|r',myString)

print(matchedPattern)