def lines(file):
    with open(file, 'r') as f:
        txt = f.readlines()
    return len(txt)
print(lines('test.txt'))