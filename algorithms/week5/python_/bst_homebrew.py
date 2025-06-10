# My attempt at prototyping a BST.

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def set_left(self, child):
    self.left = child
  
  def set_right(self, child):
    self.right = child

  def get_left(self):
    if self.left == None:
      raise KeyError
    return self.left
  
  def get_right(self):
    if self.right == None:
      raise KeyError
    return self.right
  
class BST:
  def __init_(self, node):
    self.root = node