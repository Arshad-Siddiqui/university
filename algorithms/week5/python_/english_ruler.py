# Incredibly messy implementation but it sorta works?

def draw_line(length, label=''):
    """Prints out a string of '-'s at specified length and marks it with an optional label"""
    line = "-" * length
    if label or label == 0:
        line += ' ' + str(label)
    print(line)

def draw_ruler(inches, major_length):
    for i in range(inches):
        draw_line(major_length, i)
        draw_interval(major_length)
    draw_line(major_length, inches)

def draw_interval(center_length):
    if center_length == 0:
        return
    draw_interval(center_length -1)
    draw_line(center_length)
    draw_interval(center_length - 1)
draw_ruler(6, 3)