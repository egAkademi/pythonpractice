nums = [7, 7, 7, 7, 7]
nums[2] = 5
print(nums)

nums = [1, 2, 3, 4, 5]
nums[3] = nums[1]
print(nums[3])

nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)

nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5
if 4 in nums:
  print(nums[3])
else:
  print(nums[4])