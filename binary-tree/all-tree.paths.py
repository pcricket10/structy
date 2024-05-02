# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def all_tree_paths(root):
  if root is None: return []
  if root.left is None and root.right is None: return [[root.val]]
  output = []
  left = all_tree_paths(root.left)
  for sub_path in left: output.append([root.val, *sub_path])
  right = all_tree_paths(root.right)
  for sub_path in right: output.append([root.val, *sub_path])

  return output