# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_list_values(head):
  output = []
  while(head):
    output.append(head.val)
    head = head.next
  
  
  return output
