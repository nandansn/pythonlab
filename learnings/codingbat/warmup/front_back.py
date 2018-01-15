def front_back(str):
    if(len(str) > 2):
        str = str[len(str)-1] + str[1:len(str)-1] + str[0]
    else:
        if(len(str) == 2):
            str = str[1] + str[0];

    return str

print(front_back("abc"))
