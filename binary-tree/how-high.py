# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def how_high(node):
  if node is None: return -1
  print(node.val)
  left = how_high(node.left)
  right = how_high(node.right)
  return 1 + max(left, right)