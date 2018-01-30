def big_diff(nums=[]):
    nums.sort()
    diff = nums[len(nums) - 1] - nums[0]

    return diff

nums = [10,3,5,6]
print(nums)
print(big_diff(nums))
