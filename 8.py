def longestLength(a):
    max1 = len(a[0])
    temp = a[0]
  
    # for loop to traverse the list
    for i in a:
        if(len(i) > max1):
  
            max1 = len(i)
            temp = i
    print(max1)
a = list(map(int,input().split()))
longestLength(a)