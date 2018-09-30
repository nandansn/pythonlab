'''
Given a string, return the count of the number of times that a substring length 2 
appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 
(we won't count the end substring).
'''

def last2(str):
    last2Char = str[-2:]
    count = 0
    i = 0
    for i in range(len(str)-2):
        if last2Char == str[i:i+2]:
            count = count +1
    return count


strinput = input('enter the string:')

print(last2(strinput))




