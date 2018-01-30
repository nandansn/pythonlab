def sum13(nums=[]):
    sum = 0
    for num in range(0,len(nums)):
        if nums[num] != 13:
            if num > 0:
                if nums[num - 1] != 13:
                    sum+= nums[num]
            else:
                sum+= nums[num]
        
    return sum

print(sum13([13, 1, 2, 13, 2, 1, 13]))