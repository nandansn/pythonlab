import re
import os

filePath = os.getcwd()

fileName = "\\nanda.html"

file = open(filePath+fileName)

print(filePath+fileName)

pattern =r"(^[<](\w+))"

patternObject = re.compile(pattern)

for line in file.readlines():
    #print(line)
    mathedObject = re.match(patternObject,line)
    if mathedObject != None:
        print(mathedObject.groups()[1])


