def string_splosion(str):
    newStr =""
    for i in range(len(str)+1):
        newStr = newStr + str[0:i]
    return newStr

print(string_splosion('code'))
