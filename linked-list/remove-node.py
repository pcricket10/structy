def remove_node(head, target_val):
  prev = None
  curr = head
  while curr is not None:
    print(curr.val)
    print(curr.val == target_val)
    if curr.val == target_val:
      if prev is not None:
        prev.next = curr.next
        return head
      return head.next
    prev = curr
    curr = curr.next
  return