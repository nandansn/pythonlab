def left2(str):
    if len(str) > 2:
        return str[2:len(str)] + str[0:len(str) - len(str[2:len(str)])]
    else:
        return str

print(left2("he"))
  
