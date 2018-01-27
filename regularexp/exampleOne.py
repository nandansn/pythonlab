import re

pattern = "[\d]+"

#patternObject = re.compile(pattern)

matchedObject = re.findall(r"[\d]+","abc 2 sS1 08182310")


print(matchedObject)
