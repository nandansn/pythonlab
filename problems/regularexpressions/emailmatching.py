import re

email = input("Enter Email:")

pattern = r"(\w+)(\W*)(\w*)(@{1})(\w+)(\.)(\w+)"

patternObject = re.compile(pattern)

objectMatched = re.match(patternObject,email)

if objectMatched != None:
    print(objectMatched.group())
else:
    print("Not valid email")