# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def reverse_list(head):
  curr = head
  prev = None
  while(curr):
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
  
  return prev
