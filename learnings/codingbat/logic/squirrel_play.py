def squirrel_play(temp, is_summer):
    if is_summer:
        if temp >= 60 or temp <= 100:
            return True
        else:
            return False
    else:
        if temp >= 60 or temp <= 90:
            return True
        else:
            return False

print(squirrel_play(95,False))
