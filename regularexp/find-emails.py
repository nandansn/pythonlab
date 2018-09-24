import re

inputString = input("Enter the string:")

emailsOnly = re.findall(r'[\w.]+@[\w.]+',inputString)

for email in emailsOnly:
    print(email)