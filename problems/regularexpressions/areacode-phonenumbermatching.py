import re

pattern = r"((\d){3})"

patterObject = re.compile(pattern)

phoneNumber = input("Enter phone number:")

phoneNumber ="416 555 9090"

matchedObject = re.search(patterObject,phoneNumber)

if  matchedObject != None:
    print(matchedObject.group())
else:
    print("no match found")