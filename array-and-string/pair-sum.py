def pair_sum(numbers, target_sum):
  previous = {}
  for i,num in enumerate(numbers):
    complement = target_sum - num
    if(complement in previous):
      return (previous[complement],i)
    previous[num] = i