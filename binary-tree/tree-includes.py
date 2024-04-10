# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_includes(root, target):
  if root is None: return False
  stack = [root]
  while stack:
    curr = stack.pop()
    if curr.val == target: return True
    if curr.left is not None: stack.append(curr.left)
    if curr.right is not None: stack.append(curr.right)
  return False
  