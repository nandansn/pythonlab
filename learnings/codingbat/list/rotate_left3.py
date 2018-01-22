def rotate_left3(nums=[]):
    nums.insert(len(nums),nums[0])
    del nums[0]
    return nums

print(rotate_left3([1,2,3]))
  
