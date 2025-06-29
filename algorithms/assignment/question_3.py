# Question 3: Pathfinder

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
      raise ValueError("Altitudes has incorrect width")
    if len(altitudes[0]) != len(self._map[0]):
      raise ValueError("Altitudes has incorrect height")
    
    self._map = altitudes
  

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


  def is_reachable(self, x, y):
    # Doesn't change the board.
    pass