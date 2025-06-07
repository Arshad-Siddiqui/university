import os

def disk_usage(directory):
    """Directory: A string of the relevant directory path"""
    # We start with the disk usage of the current directory
    total = os.path.getsize(directory)
    # We check if it is a directory before trying to look inside.
    if os.path.isdir(directory):
        for filename in os.listdir(directory):
            # File name doesn't come with full path so we
            # link it with the directory path so we can use it.
            childpath = os.path.join(directory, filename)
            total += disk_usage(childpath)
    return total

# Could implement sys package so we can
# give the file some arguments from the command line.
print(disk_usage(""))