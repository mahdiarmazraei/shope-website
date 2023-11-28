import math

def av(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i == 0:
            return True
    return False

a = int(input())
b = int(input())
aval = 0
for i in range(a,b+1):
    if not av(i):
        aval += 1

kol = b - a + 1
print('{}%'.format(int(aval/kol*100)))


