import math
adad = int(input("please inter yuor number"))

jazr = int(adad / 2)

a = []
x = 2
while x != jazr + 1:
    if adad % x != 0:
        x += 1
    else:
        adad = adad / x
        a.append(x)
print (a)

    