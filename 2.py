def file(f, n):
        from itertools import islice
        with open(f) as s:
                for i in islice(s,n):
                        print(i)
a=input()
file('test.txt',a)