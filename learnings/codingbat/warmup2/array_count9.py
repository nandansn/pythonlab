def array_count9(nums):
  countnine = 0;
  for num in nums:
      if num == 9:
        countnine = countnine + 1
  return countnine

print(array_count9([1,2,3,9,2,9,9]))


