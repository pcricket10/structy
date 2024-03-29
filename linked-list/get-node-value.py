# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def get_node_value(head, index):
  i = 0
  while(head):
    if i == index:
      return head.val
    i += 1
    head = head.next