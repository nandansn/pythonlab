import re
import os

filePath = os.getcwd()

#fileName = "\\problems\\regularexpressions\\nanda.html"

fileName = "\\nanda.html"

file = open(filePath+fileName)

print(filePath+fileName)

pattern =r"(>(\w+\W*)+<)"

patternObject = re.compile(pattern)

for line in file.readlines():
    mathedObject = re.search(patternObject,line)
    if mathedObject != None:
        print(mathedObject)


