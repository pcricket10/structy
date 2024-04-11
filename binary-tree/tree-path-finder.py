# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def path_finder(root, target):
  if root is None: return None
  if root.val == target: return [target]
  left = path_finder(root.left, target)
  right = path_finder(root.right, target)
  if left is not None: return [root.val, *left]
  if right is not None: return [root.val, *right]
  return None
