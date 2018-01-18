def count_code(str=""):
    countCode = 0;
    for i in range(0,len(str)-3):
        newStr = str[i:i+4]
        print(newStr)
        if ( newStr.startswith("co") and newStr.endswith("e")):
            countCode = countCode + 1
    return countCode

print(count_code('aaacoeebbbcode'))