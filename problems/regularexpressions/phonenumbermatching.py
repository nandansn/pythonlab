import re

phoneNumber = input("Enter Phone Number:")

pattern =r"[\(]?(\d{3})(-|\))(\d{3})-(\d{4,4})"

patternObject = re.compile(pattern)

matchedObject = re.fullmatch(patternObject,phoneNumber)

if matchedObject != None:
    print(matchedObject.group())
else:
    print("Not Valid Number")