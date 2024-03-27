def anagrams(s1, s2):
  count = {}
  for char in s1:
    if char not in count:
      count[char] = 1
    else:
      count[char] +=1
    
  for char in s2:
    if char not in count:
      return False
    if count[char] == 1:
      del(count[char])
    else:
      count[char] -= 1
  print(count)
  return count == {}