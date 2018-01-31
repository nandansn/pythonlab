def sum67(nums=[]):
    flag = True
    sum = 0
    for num in nums:
        if flag:
            if num == 6:
                flag = False
            else:
                sum+= num
        else:
            if num == 7:
                flag = True
    return sum

print(sum67([1, 1, 6, 7, 2]))