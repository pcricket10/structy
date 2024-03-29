def most_frequent_char(s):
  count = {}
  max_char = ""
  max_val = 0
  for char in s:
    if char not in count:
      count[char] = 1
    else:
      count[char] += 1
  for curr in count:
    if count[curr] > max_val:
      max_val = count[curr]
      max_char = curr
  return max_char