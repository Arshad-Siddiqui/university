# Incredibly messy implementation but it sorta works?

def draw_line(length, label=''):
    """Prints out a string of '-'s at specified length and marks it with an optional label"""
    line = "-" * length
    if label:
        line += ' ' + str(label)
    print(line)

def draw_ruler(inches, major_length):
    for i in range(inches):
        draw_line(major_length, str(i))
        draw_interval(major_length)
    draw_line(major_length, str(inches))
    
def draw_interval(major_length):
    if major_length <= 1:
        return
    draw_interval(major_length -1)
    draw_line(major_length - 1)
    draw_interval(major_length - 1)
draw_ruler(3, 5)