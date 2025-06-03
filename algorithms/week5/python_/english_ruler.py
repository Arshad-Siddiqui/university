# English Ruler and Recursion

def draw_ruler(length):
  if length == 1:
    return

  remainder = length % 4
  print(remainder * '-')
  draw_ruler(length - 1)
draw_ruler(8)