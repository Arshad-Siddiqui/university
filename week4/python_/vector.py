import copy

# Exercise 1

class Vector:
  def __init__(self, data):
    """Stores a shallow copy of the list passed in parameters: data -> a list of floats"""
    self.data = copy.copy(data)

# Exercise 2
  def __str__(self):
    return str(self.data).replace('[', '<').replace(']', '>')
  
# Exercise 3
  def dim(self):
    return len(self.data)
  
# Exercise 4
  def get(self, index):
    return self.data[index]
  
  def set(self, index, value):
    self.data[index] = value

# Exercise 5

  def scalar_product(self, number):
    multiplied = []
    for element in self.data:
      multiplied.append(element * number)

    return Vector(multiplied)
    
# Exercise 6

  def __add__(self, other):
    if not isinstance(other, Vector):
      return None
    if other.dim() != self.dim():
      return None
    # Guard clauses above checking if we're adding another vector and they're the same dimension
    added = []
    for i in range(self.dim()):
      added.append(self.data[i] + other.data[i])
    return Vector(added)
  
# Exercise 7
  def equals(self, other):
    if not isinstance(other, Vector):
      return None
    
    ## Note: Come back when you aren't tired

vec1 = Vector([2.3, 1.0, 9.7])
print(vec1)
print('vec1 dimention: ' + str(vec1.dim()))
print('vec1 * 3' + str(vec1.scalar_product(3)))

vec2 = Vector([7.7, 3.0, 0.3])

print(vec1 + vec2)