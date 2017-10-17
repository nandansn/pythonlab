def pos_neg(a, b, negative):
    if (negative and a<0 and b<0):
        return "True"
    elif ((a <0 or b<0) and  negative == False ):
        return "True"
    elif (not negative and a<0 and b<0):
        return False
    else:
      return False

def test(negative):
    if(1 < 2  and not negative):
        print("true")

def not_string(str):

    if (str.find("not",0,3) > -1):
        return str
    else:
        return 'not '+str

print(not_string("not bas"))

