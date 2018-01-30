import re

count = int(input("Enter Numbers:"))

pattern = r"^[Hh][Ii][\s][^D^d].*"

patternObject = re.compile(pattern)


for i in range(count):
    sentence = input()
    matchedObject = re.match(patternObject,sentence)
    if matchedObject != None:
        print(matchedObject)

