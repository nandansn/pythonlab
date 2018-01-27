def near_ten(num=0):
    remainder = (num%10)
    if remainder <= 2:
        return True
    elif (10 - remainder <= 2):
        return True
    else:
        return False
        
    
