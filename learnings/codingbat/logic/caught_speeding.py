def caught_speeding(speed, is_birthday):
    if not is_birthday:
        if speed <= 60:
            return 0
        elif speed > 60 and speed < 81:
            return 1
        else:
            return 2
    else:
        if speed <= 60+5:
            return 0
        elif speed > 60+5 and speed < 81+5:
            return 1
        else:
            return 2

print(caught_speeding(65, True))