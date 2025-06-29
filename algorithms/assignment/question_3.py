# Question 3: Pathfinder
import copy
from queue import Queue

class PathFinder():
  def _validate_xy(self, x, y):
    """
    Private helper function that validates a given set of coordinates by checking if they are within bounds.

    Args:
      x (int): Row index
      y (int): Column index

    Raises:
      ValueError: If coordinates are ouf of map bounds
    """
    if x >= len(self._map) or x < 0:
      raise ValueError(f"X needs to be within bounds. x: {x}")
      
    if y >= len(self._map[0]) or y < 0:
      raise ValueError(f"Y needs to be within bounds. y: {y}")
    
  
  def __init__(self, width=5, height=5, rover_x=0, rover_y=0, rover_max_gradient=1):
    """
    Initialises new rover instance with 2d map, rover position and maximum gradient.

    Args:
      width (int): Width of the map. Minimum length of 5 and defaults to 5.
      height (int): Height of the map. Minimum length of 5 and defaults to 5.
      rover_x (int): Index representing the Rover's x position on the map. Must be within bounds.
      rover_y (int): Index representing the Rover's y position on the map Must be within bounds.
      rover_max_gradient (int): Maximum gradient the rover can traverse.
    
    Raises:
      ValueError: When height and width are less than 5, rover is out of bounds or max-gradient is 0 or less.
    """
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
    """
    Returns altitude at given coordinates after checking the arguments are within bounds.

    Args:
      x (int): x coordinate to be checked.
      y (int): y coordinate to be checked.

    Raises:
      ValueError: When given x or y are out of bounds.

    Returns:
      int: Integer that represents altitude at the specified position. -1 means it is untraversable and -2 means it can be mined.
    """
    self._validate_xy(x, y)
    return self._map[x][y]
    

  def set_altitude(self, x, y, altitude):
    """
    Changes the altitude of given coordinates after validation.

    Args:
      x (int): x coordinate of position to be changed.
      y (int): y coordinate of position to be changed.
      altitude (int): The altitude that the given position should now be.
    
    Raises:
      ValueError: When given coordinates are incorrect. Or altitude is too low.
    """
    self._validate_xy(x, y)
    if altitude < -2:
      raise ValueError("Values can't be less than -2")
    self._map[x][y] = altitude
  

  def set_terrain(self, altitudes):
    """
    Replaces the entire 2d map with a new one provided the dimensions are the same. Creates a deep copy of it.

    Args:
      Altitudes (int[int[]]): 2d array containing integers the same size as the one stored.
    
    Raises:
      ValueError: When the new 2d array is of different dimensions to the original.
    """
    if len(altitudes) != len(self._map):
      raise ValueError("Altitudes has incorrect height")
    
    for i in range(len(self._map)):
      if len(altitudes[i]) != len(self._map[i]):
        raise ValueError(f"Altitudes has incorrect width in row {i}")
    
    # Avoids aliasing external list
    self._map = copy.deepcopy(altitudes)
  

  def get_resources(self):
    """
    Returns set containing tuples of coordinates that have resources.

    Returns:
      tuple(int): Set of tuples containing positions that can be mined.
    """
    resource_positions = set()
    for x in range(len(self._map)):
      for y in range(len(self._map[0])):
        if self._map[x][y] == -2:
          resource_positions.add((x, y))
    return resource_positions
  

  def get_rover(self):
    """
    Returns tuple containing the current position of the rover.

    Returns:
      tuple(int): Tuple containing the coordinates of the the rover's current position.
    """
    return self._rover_position
  

  def set_rover(self, x, y):
    """
    Moves the rover and raises an error if that move is not performable.

    Args:
      x (int): x coordinate that the rover should move to.
      y (int): y coordinate that the rover should move to.

    Raises:
      ValueError: When the specified position is either out of bounds or on an untraversable position.
    """
    self._validate_xy(x, y)

    if self.get_altitude(x, y) == -1:
      raise ValueError("Rover can't be put on untraversable position")
    self._rover_position = (x, y)

  
  def move_rover(self, x, y):
    """
    Moves rover and returns boolean specifying if move was successful.

    Args:
      x (int): x coordinate where the rover should be moved.
      y (int): y coordinate where teh rover should be moved.
    Returns:
      bool: True when the rover has successfully moved or false if unsuccessful.
    """
    self._validate_xy(x, y)
    if self.get_altitude(x, y) == -1:
      return False
    self.set_rover(x, y)
    return True


  # Doesn't change the board. Returns bool
  def isreachable(self, x, y):
    """
    Figures out if a given position is accessible, using Breadth First Search, to the rover from its current position.

    Args:
      x (int): x coordinate of position to be tested. 
      y (int): y coordinate of position to be tested.

    Returns:
      Bool: If given position is reachable it returns True otherwise False.
    """
    positions = Queue()
    visited = set()

    # starting position goes in queue and is obviously visited
    positions.put(self.get_rover())
    visited.add(self.get_rover()) 
    # Keep going while there are positions in the queue
    while not positions.empty():
      # Dequeues that element first in line
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
  

  def get_closest_resource(self):
    """
    Utilises Breadth First Search to exhaustively check which reachable resource is closest to the rover.

    Returns:
      tuple or None: A tuple containing the coordinates to the closest resource or if none are reachable then it returns None.
    """
    resources = self.get_resources()
    position = self.get_rover()
    # Gets replaced during iteration with closer resources
    closest_resource = None
    for resource in resources:
      # if resource is unreachable continue
      if not self.isreachable(resource[0], resource[1]):
        continue
      # First reachable resource needs no comparison
      if closest_resource == None:
        closest_resource = resource
      else:
        # Distance of the current closest resource
        closest_resource_dx = abs(position[0] - closest_resource[0])
        closest_resource_dy = abs(position[1] - closest_resource[1])
        closest_distance = closest_resource_dx + closest_resource_dy

        # Distance of the challenging resource
        resource_dx = abs(position[0] - resource[0])
        resource_dy = abs(position[1] - resource[1])
        resource_distance = resource_dx + resource_dy

        # If distance is shorter we replace closest resource
        if resource_distance < closest_distance:
          closest_resource = resource
    return closest_resource