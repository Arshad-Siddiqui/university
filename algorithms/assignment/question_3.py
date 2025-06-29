# Question 3: Pathfinder
import copy
from queue import Queue

class PathFinder():
  def _validate_xy(self, x, y):
    if x >= len(self._map) or x < 0:
      raise ValueError(f"X needs to be within bounds. x: {x}")
      
    if y >= len(self._map[0]) or y < 0:
      raise ValueError(f"Y needs to be within bounds. y: {y}")
    
  
  def __init__(self, width=5, height=5, rover_x=0, rover_y=0, rover_max_gradient=1):
    if width < 5 or height < 5:
      raise ValueError("Width and height can't be less than 5")
    
    self._map = []
    for _ in range(height):
      self._map.append([0 for _ in range(width)])
    
    self._validate_xy(rover_x, rover_y)
    
    self._rover_position = (rover_x, rover_y)

    if rover_max_gradient <= 0:
      raise ValueError("Rover max gardient can't be 0 or less")

    self._rover_max_gradient = rover_max_gradient
  

  def get_altitude(self, x, y):
    self._validate_xy(x, y)
    return self._map[x][y]
    

  def set_altitude(self, x, y, altitude):
    self._validate_xy(x, y)
    self._map[x][y] = altitude
  

  def set_terrain(self, altitudes):
    if len(altitudes) != len(self._map):
      raise ValueError("Altitudes has incorrect height")
    
    for i in range(len(self._map)):
      if len(altitudes[i]) != len(self._map[i]):
        raise ValueError(f"Altitudes has incorrect width in row {i}")
    
    # Avoids aliasing external list
    self._map = copy.deepcopy(altitudes)
  

  def get_resources(self):
    resource_positions = set()
    for x in range(len(self._map)):
      for y in range(len(self._map[0])):
        if self._map[x][y] == -2:
          resource_positions.add((x, y))

    return resource_positions
  

  def get_rover(self):
    return self._rover_position
  

  def set_rover(self, x, y):
    self._validate_xy(x, y)

    if self.get_altitude(x, y) == -1:
      raise ValueError("Rover can't be put on untraversable position")
    self._rover_position = (x, y)

  
  def move_rover(self, x, y):
    self._validate_xy(x, y)
    if self.get_altitude(x, y) == -1:
      return False
    self.set_rover(x, y)
    return True


  # Doesn't change the board. Returns bool
  def is_reachable(self, x, y):
    positions = Queue()
    visited = set()

    # starting position goes in queue and is obviously visited
    positions.put(self.get_rover())
    visited.add(self.get_rover()) 
    # Keep going while there are positions in the queue
    while not positions.empty():
      current_position = positions.get()
      if current_position == (x, y):
        return True
      
      cx, cy = current_position
      neighbours = [(cx, cy+1), (cx, cy-1), (cx-1, cy), (cx+1, cy)]

      for neighbour in neighbours:
        if neighbour not in visited:
          try:
            self._validate_xy(neighbour[0], neighbour[1])
          except ValueError:
            continue
          if self.get_altitude(neighbour[0], neighbour[1]) != -1:
            gradient = abs(self.get_altitude(neighbour[0], neighbour[1]) - self.get_altitude(current_position[0], current_position[1]))
            if gradient <= self._rover_max_gradient:
              visited.add(neighbour)
              positions.put(neighbour)
    return False