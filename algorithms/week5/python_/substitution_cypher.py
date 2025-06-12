import copy

simple_cypher = {
    'a': 'z',
    'b': 'a',
    'c': 'b',
    'd': 'c',
    'e': 'd',
    'f': 'e',
    'g': 'f',
    'h': 'g',
    'i': 'h',
    'j': 'i',
    'k': 'j',
    'l': 'k',
    'm': 'l',
    'n': 'm',
    'o': 'n',
    'p': 'o',
    'q': 'p',
    'r': 'q',
    's': 'r',
    't': 's',
    'u': 't',
    'v': 'u',
    'w': 'v',
    'x': 'w',
    'y': 'x',
    'z': 'y',
    ' ': ' '
}

def encrypt_message(message, cypher_dict):
  new_arr = []
  
  for char in message:
    if char in cypher_dict:
      new_arr.append(cypher_dict[char])
    else:
      new_arr.append(char)
  return ''.join(new_arr)

print(encrypt_message("secret message", simple_cypher))

def decrypt_message(message, cypher_dict):
  cypher_copy = copy.copy(cypher_dict)
  cypher_copy = dict((value, key) for key, value in cypher_copy.items())

  new_arr = []
  
  for char in message:
    if char in cypher_copy:
      new_arr.append(cypher_copy[char])
    else:
      new_arr.append(char)
  return ''.join(new_arr)

print(decrypt_message("rdbqds ldrrzfd", simple_cypher))