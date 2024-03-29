def intersection(a, b):
  items_set = set(a)
  
  
  # output = []
  # for val in a:
  #   items_set.add(val)
  # for ele in b:
  #   if ele in items_set:
  #      output.append(ele)
  # return output
  
  return [ ele for ele in b if ele in items_set]