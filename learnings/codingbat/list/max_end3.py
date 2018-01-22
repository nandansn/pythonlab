def max_end3(nums=[]):
    replaceNum = -1
    if nums[0] > nums[len(nums)-1] :
        replaceNum = nums[0]
    else:
        replaceNum = nums[len(nums)-1]
    for i in range(0,len(nums)):
        nums.remove(nums[0])
        nums.append(replaceNum)
        
    return nums

print(max_end3([1,2,3]))
  
