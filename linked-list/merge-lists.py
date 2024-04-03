class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def merge_lists(head_1, head_2):
  dummy = Node(None)
  tail = dummy
  curr1 = head_1
  curr2 = head_2
  while curr1 is not None and curr2 is not None:
    if curr1.val > curr2.val:
      tail.next = curr2
      curr2 = curr2.next
    else:
      tail.next = curr1
      curr1 = curr1.next
    tail = tail.next
  if curr1 is not None:
    tail.next = curr1
  if curr2 is not None:
    tail.next = curr2
  return dummy.next
    
