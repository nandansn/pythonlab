import re

numbers = input("Enter Number:")

pattern = r"^[-]?[\d]+[,]*[\d]+[\.]?[e]?[\d]+$"

patternObject = re.compile(pattern)

patternMatched = re.match(pattern,numbers)

print(patternMatched)




