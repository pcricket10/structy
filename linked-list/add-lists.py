class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def add_lists(head_1, head_2):
  # ones place first, then tens, etc
  dummy = Node(None)
  tail = dummy
  curr1 = head_1
  curr2 = head_2
  carry = 0
  while curr1 is not None or curr2 is not None or carry == 1:
    # print(output.val)
    if curr1 is None:
      val1 = 0
    else:
      val1 = curr1.val
    if curr2 is None:
      val2 = 0
    else:
      val2 = curr2.val
    curr_sum = val1 + val2 + carry
    if curr_sum > 9:
      curr_sum = curr_sum % 10
      carry = 1
    else:
      carry = 0
      
    tail.next = Node(curr_sum)
    tail = tail.next
    if curr1 is not None:
      curr1 = curr1.next
      # tail.next = curr1
    if curr2 is not None:
      curr2 = curr2.next
      # tail.next = curr2
  if carry == 1:
    tail.next = Node(1)
  return dummy.next