def uncompress(s):
  digits = "0123456789"
  i = 0;
  j = 0;
  output = []
#   pointers
  while j < len(s):
    if s[j] in digits:
      j += 1
    else:
      output.append(s[j] * int(s[i:j]))
      j+=1
      i=j

  return ''.join(output)


