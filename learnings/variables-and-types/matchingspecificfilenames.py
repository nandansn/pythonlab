import re

fileName = input("Enter File Name")

pattern = r"(\w+)\.(jpg|png|gif)"

patternObject = re.compile(pattern)

for match in re.finditer(patternObject,fileName):
    print(match)