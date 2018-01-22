def has23(nums=[]):
    nums.sort()
    for num in nums:
        if num == 2 or num == 3:
            return True
    return False

