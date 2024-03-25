def compress(s):
  s += "!"
  output = ""
  i = 0
  j = 0
  while j < len(s):
    if s[i] == s[j]:
      j += 1
    else:
      if(j-i != 1):
        output += str(j-i)
      output += s[i]
      i = j
  return output