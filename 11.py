import os
def file(f):
    size = os.stat(f).st_size
    return size

print(file('text.txt'))