class ArrayStack:
  def __init__(self):
    self.array = []

  def push(self, value):
    self.array.append(value)

  def pop(self):
    return self.array.pop()
  
  def top(self):
    return self.array[-1]