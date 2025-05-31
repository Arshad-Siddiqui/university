import math
import copy
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def print_coords(self):
    print(f"({self.x}, {self.y})")


def distance(point1, point2):
  return math.sqrt(((point1.x-point2.x)**2) + ((point1.y - point2.y)**2))

def move_point(point, dx, dy):
  new_point = copy.deepcopy(point)
  new_point.x += dx
  new_point.y += dy