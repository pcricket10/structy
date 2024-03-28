def pair_product(numbers, target_product):
    previous = {}
    for i,num in enumerate(numbers):
      complement = target_product / num
      if(complement in previous):
        return (previous[complement],i)
      previous[num] = i