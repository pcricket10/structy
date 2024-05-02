# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
from collections import deque

def bottom_right_value(root):
  queue = deque([root])
  curr = None
  while queue:
    # append, popleft
    
    curr = queue.popleft()
    print(curr.val)
    if curr.left: queue.append(curr.left)
    if curr.right: queue.append(curr.right)
  return curr.val