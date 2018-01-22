def make_ends(nums=[]):
    newNums =[]
    if len(nums) > 1:
         newNums.append(nums[0])
         newNums.append(nums[1])
         return newNums
    else:
        newNums.append(nums[0])
        return newNums

print(make_ends([1,2,3]))