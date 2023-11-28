a = []
au = []
test = []
for i in range(97,123):
    a.append(chr(i))
for i in range(65,91):
    au.append(chr(i))

x = input("please inter")

for i in x:
    if i in a or i in au:
        test.append(i)
print(test)
flag = True
x = len(test)

for i in range(len(test) // 2):
    if test[i] != test[x-1-i] and test[i] != test[x-1-i].upper() and test[i] != test[x-1-i].lower():
        flag = False
print(flag)



