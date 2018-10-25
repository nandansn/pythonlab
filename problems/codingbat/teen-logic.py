def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    if n in [13,14,17,18,19]:
        return 0
    else:
        return n

print(no_teen_sum(1,2,14))