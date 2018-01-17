def array123(nums):

    for i in range(0,len(nums)-2):
      if(nums[i] == 1 ):
          if (nums[i+1] == 2):
              if(nums[i+2] == 3):
                  return True;
    return False

print(array123([1,1,2,1]))


