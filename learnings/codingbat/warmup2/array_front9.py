def array_front9(nums):

    if (nums.__len__() < 4):
        for num in nums:
            if num == 4:
                return True
    else:
        for num in range(0,4):

            if nums[num] == 4:
                return True
        return False

    return False

print(array_front9([1,2,4]))

