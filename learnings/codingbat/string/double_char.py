def double_char(str):
    newStr =""
    for c in str:
        newStr = newStr + (c * 2)
    return newStr

print(double_char("The"))