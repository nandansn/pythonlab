def first_last6(nums=[]):
    if not nums:
        return False
    else:
        if (nums.pop() == 6 or nums[0] == 6):
            return True
        else:
            return False
        
    
print(first_last6([])) 
