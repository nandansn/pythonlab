def monkey_trouble(a_smile,b_smile):
    if a_smile and b_smile:
        return True

    if a_smile is False and b_smile is False:
        return True

    if a_smile is False or b_smile is False:
        return False

