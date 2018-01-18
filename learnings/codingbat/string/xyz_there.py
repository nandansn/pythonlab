def xyz_there(str=""):
    xyzIndex =0
    i = 0
    flag = False
    str.count("xyz")
    for i in range (0,str.count("xyz")):
        if (str[0:len(str)].find("xyz") != -1):
            xyzIndex = str[0:len(str)].index("xyz")
            if (str[xyzIndex - 1 ] == '.'):
                flag = False                
            else:
               flag = True
        else:
            flag = False
        xyzIndex = xyzIndex + 2
        str = str[xyzIndex:len(str)]
    return flag

print(xyz_there('abcxyz'))