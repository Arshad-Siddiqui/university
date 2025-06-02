# Lilian Blot's code. Very different to how I would have done it.

class LinkedNode:
  """Node used for our linked list"""

  def __init__(self, data=None, next=None):
    self._data = data
    if next is None or isinstance(next, LinkedNode):
      self._next = next
    else:
      raise TypeError("Node type object expected") 
  
  @property
  def data(self):
    return self._data
  
  @data.setter
  def data(self, value):
    self._data = value

  @property
  def tail(self):
    return self._next
  
  @tail.setter
  def tail(self, node):
    if node is None or isinstance(node, LinkedNode):
      self._next = node
    else:
      raise TypeError("node type expected")
  
class LinkedList:
  def __init__(self):
    self._front = None
    self._tail = None
    self._size = 0

  def append(self, value):
    newnode = LinkedNode(value)
    if self._front is None:
      self._front = newnode
      self._tail = newnode
    else:
      self._tail.tail = newnode
      self._tail = newnode
    self._size += 1

  def pop(self):
    if self._size == 0:
      raise IndexError("List is empty")
    front_node = self._front
    self._front = self._front.tail
    front_node.tail = None
    self._size -= 1
    return front_node.data