def file(f):
        with open(f) as a:   
                b = a.readlines()
                print(b)
file('text.txt')