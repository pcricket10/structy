# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_min_value(root):
  min = root.val
  stack = [root]
  while stack:
    curr = stack.pop()
    if curr.val < min: min = curr.val
    if curr.left: stack.append(curr.left)
    if curr.right: stack.append(curr.right)
  return min