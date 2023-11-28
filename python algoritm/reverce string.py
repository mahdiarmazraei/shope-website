from stac import Stack

x = input("please_select")
z = ""
y = Stack()
for i in x:
    y.push(i)

for i in range(y.size()):
    z = z + y.pop()

print(z)
