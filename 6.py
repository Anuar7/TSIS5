def file(f):
        with open (f, "r") as myfile:
                data=myfile.readlines()
                print(data)
file('test.txt')
