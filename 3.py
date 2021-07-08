def file(n):
    with open(n, 'w') as a:
        a.write('Hello KBTU')
    txt = open(n)
    print(txt.read())
file('text.txt')