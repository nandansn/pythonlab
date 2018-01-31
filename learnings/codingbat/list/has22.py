def has22(nums=[]):
    has22Flag = False
    for num in nums:
        if has22Flag:
            if num == 2:
                return True
            else:
                has22Flag = False
        else:
            if num == 2:
                has22Flag = True
            else:
                has22Flag = False
    return has22Flag

print(has22([1, 2, 1,2]))