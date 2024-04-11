# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_value_count(root, target):
  if root is None: return 0
  count = 0
  stack = [root]
  while stack:
    curr = stack.pop()
    if curr.val == target: count += 1
   
    if curr.left: stack.append(curr.left)
    if curr.right: stack.append(curr.right)
  return count