def five_sort(nums):
  five_count = 0
  i = 0
  while i < len(nums):
    if nums[i] == 5:
      nums.pop(i)
      five_count += 1
    else:
      i += 1
  for i in range(five_count):
    nums.append(5)
  return nums