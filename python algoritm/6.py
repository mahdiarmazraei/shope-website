x = "hello"
for i in range(len(x)):
    x = x[-1:] + x[:-1]
    print(x)