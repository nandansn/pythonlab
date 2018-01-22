def sum2(nums=[]):
    sum = 0
    if not nums:
        return sum
    else:
        if len(nums) < 2:
            return nums[0]
        else:
            for i in range(0,2):
                sum = sum + nums[i]
        return sum

print(sum2([]))


  
