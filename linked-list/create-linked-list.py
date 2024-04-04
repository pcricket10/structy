class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def create_linked_list(values):
  head = Node(None)
  curr = head
  for value in values:
    curr.next = Node(value)
    curr = curr.next
  return head.next