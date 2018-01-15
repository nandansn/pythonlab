def last2(str):
    substr=""
    str=""
    count=0;
    for i in range(len(str)-3):
        print(str[i:i+2])
        if (str.find(str[i:i+2],0,len(str))):
            count = count +1
    return count;


print(last2('hixxhi'))


