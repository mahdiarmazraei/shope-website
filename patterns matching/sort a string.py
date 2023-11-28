x = [[[1, 2, 3], 2, [3, 4]], 5]

for key, value in enumerate(x):
    print (key)
    if isinstance(x[key], list):
        for i,j in enumerate(x[key]):
            print (i)
