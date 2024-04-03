# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def longest_streak(head):
  if head is None:
    return 0
  max_streak = 1
  curr_streak = 1
  # curr_val = head.val
  curr = head
  while curr.next:
    if curr.val == curr.next.val:
      curr_streak += 1
    else:
      curr_streak = 1
      curr.val = curr.next.val
    if curr_streak > max_streak:
      max_streak = curr_streak
    curr = curr.next
  return max_streak