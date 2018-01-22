def same_first_last(nums=[]):
    if not nums:
        return False
    else:
        if (nums[0] == nums.pop()):
            return True
        else:
            return False

print(same_first_last([]))

