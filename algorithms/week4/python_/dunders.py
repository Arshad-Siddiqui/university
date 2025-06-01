# 4.2.6 notes

class GameLog:
  def __init__(self):
    self._games = []
  
  def add_game(self, game):
    self._games.append(game)

  def __getitem__(self, index):
    return self._games[index]
  
  def __setitem__(self, index, value):
    self._games[index] = value

  def __delitem__(self, index):
    del self._games[index]

  def __len__(self):
    return len(self._games)
  
  def __repr__(self):
  # chatgpt suggested i add !r at the end
    return f"GameLog({self._games!r})"
  # These ones make this list iterable

  def __contains__(self, game):
    return game in self._games

  def __iter__(self):
    self._current_index = 0
    return self
  
  def __next__(self):
    if self._current_index < len(self._games): 
      current_game = self._games[self._current_index]
      self._current_index += 1
      return current_game
    else:
      raise StopIteration

backlog = GameLog()

games = ['Crash', 'Mario', 'Spyro', 'Rayman']

print('before games were added to backlog')
print(repr(backlog))
print('-----')

for game in games:
  backlog.add_game(game)

print('games added to backlog')
print(repr(backlog))

assert backlog[1] == 'Mario'

backlog[1] = 'Sonic'

assert backlog[1] == 'Sonic'

print(repr(backlog))

del backlog[3]
print('item at position 3 deleted \n ----')
print(repr(backlog))

for i in range(len(backlog)):
  print(f"{i + 1}) {backlog[i]}")

print("if crash is in backlog print crash!")

if "Crash" in backlog:
  print("Crash!!!")