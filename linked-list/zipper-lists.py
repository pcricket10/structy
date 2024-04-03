# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def zipper_lists(head_1, head_2):
  tail = head_1
  curr1 = head_1.next
  curr2 = head_2
  count = 0
  while curr1 is not None and curr2 is not None:
    if count%2 == 0:
      tail.next = curr2
      curr2 = curr2.next
    else:
      tail.next = curr1
      curr1 = curr1.next
    count += 1
    tail = tail.next
  if curr1 is not None:
    tail.next = curr1
  if curr2 is not None:
    tail.next = curr2

  return head_1
