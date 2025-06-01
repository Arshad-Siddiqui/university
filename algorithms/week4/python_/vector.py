import copy
import math
# Exercise 1

class Vector:
  def __init__(self, data):
    """Stores a shallow copy of the list passed in parameters: data -> a list of floats"""
    self._vector = copy.copy(data)

# Exercise 2
  def __str__(self):
    return str(self._vector).replace('[', '<').replace(']', '>')
  
# Exercise 3
  def dim(self):
    return len(self._vector)
  
# Exercise 4
  def get(self, index):
    return self._vector[index]
  
  def set(self, index, value):
    self._vector[index] = value

# Exercise 5

  def scalar_product(self, number):
    multiplied = []
    for element in self._vector:
      multiplied.append(element * number)

    return Vector(multiplied)
    
# Exercise 6

  def add(self, other):
    self + other
    
  def __add__(self, other):
    if not isinstance(other, Vector):
      return None
    if other.dim() != self.dim():
      return None
    # Guard clauses above checking if we're adding another vector and they're the same dimension
    added = []
    for i in range(self.dim()):
      added.append(self._vector[i] + other._vector[i])
    return Vector(added)
  
# Exercise 7
  def equals(self, other):
    if not isinstance(other, Vector):
      return None
    
    for i in range(self.dim()):
      if not math.isclose(self.get(i), other.get(i)):
        return False
      return True
    
# Exercise 8
  def __eq__(self, other):
    if not isinstance(other, Vector):
      return None
    
    for i in range(self.dim()):
      if not math.isclose(self.get(i), other.get(i)):
        return False
      return True
    
  def __ne__(self, other):
    if not isinstance(other, Vector):
      return None
    
    for i in range(self.dim()):
      if not math.isclose(self.get(i), other.get(i)):
        return True
      return False

# Exercise 9:
  def __mul__(self, number):
    return self.scalar_product(number)
  
  def __iadd__(self, number):
    return self + number

vec1 = Vector([2.3, 1.0, 9.7])
print(vec1)
print('vec1 dimention: ' + str(vec1.dim()))
print('vec1 * 3' + str(vec1.scalar_product(3)))

vec2 = Vector([7.7, 3.0, 0.3])
vec3 = copy.copy(vec2)

print(vec1 + vec2)

print("check that vec2 and vec 2 are equal")
print(vec2.equals(vec3))

print("check that vec1 and vec3 are equal")
print(vec1.equals(vec3))