def file(f):
        arr = []
        with open(f) as a:     
                for line in a:
                        arr.append(line)
                print(arr)
file('test.txt')