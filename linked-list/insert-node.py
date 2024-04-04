class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def insert_node(head, value, index):

  i = 1
  curr = head
  new_node = Node(value)
  if index == 0:
    new_node.next = head
    return new_node
  while curr is not None:
    if i == index:
      next = curr.next
      curr.next = new_node
      new_node.next = next
      return head

    curr = curr.next
    i+=1
