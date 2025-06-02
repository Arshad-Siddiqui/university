# Big mess come back to 4.4.3 activity

class Stack:
  def __init__(self, size=1000):
    self.array = []

  def push(self, value):
    self.array.append(value)

  def pop(self):
    return self.array.pop()
  
  def top(self):
    return self.array[-1]
  
  def is_empty(self):
    return len(self.array) == 0
  
def is_matched(expr):
  '''Return True if all delimiters are correctly matched; False otherwise'''
  s = Stack()
  left = '({[' # opening delimiters
  right = ')}]' # closing delimiters
  for c in expr:
    if c in left:
      s.push(c) # push left delimiters to stack
    elif c in right:
      if s.is_empty():
        return False # no matching opening delimiter
      if right.index(c) != left.index(s.pop()):
        return False # mismatched delimiter
    return s.is_empty() # were all symbols matched? True/False
  
print(is_matched("(())}"))
print(is_matched("()"))