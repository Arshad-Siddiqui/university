# Comparing classes

class StopWatch:
  def __init__(self, seconds):
    self._seconds = seconds

  def to_minutes(self):
    minutes = int(self.seconds / 60)
    seconds = self.seconds % 60

    return f'{minutes:02}:{seconds:02}'
  
  def __eq__(self, other):
    if isinstance(other, StopWatch):
      return self._seconds == other._seconds
    return False
  
  def __lt__(self, other):
    if isinstance(other, StopWatch):
      return self._seconds < other._seconds
    raise TypeError("Comparison incompatible with this type")

  # ------------
  # Everything below this line is ctrl c + v
  
  def __ne__(self, other):
        return not self == other

  def __le__(self, other):
        return self == other or self < other
    
  def __ge__(self, other):
        return self == other or not self < other
    
  def __gt__(self, other):
        return self != other and not self < other
    
  def __repr__(self):
        return f"RomanNumeral({self.value})"
