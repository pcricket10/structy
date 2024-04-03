# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def is_univalue_list(head):
  value = head.val
  curr = head.next
  while curr:
    if curr.val != value: return False
    curr = curr.next
  return True
