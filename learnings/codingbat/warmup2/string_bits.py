def string_bits(str):
    newStr =""
    for i in range(0,len(str),2):
        newStr = newStr + str[i]
    return newStr


print(string_bits("Hello"))
