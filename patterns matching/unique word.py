from collections import Counter

f = open("test.txt", "r")
words = f.read()
words = words.split()
words = [word.upper() for word in words]
count = Counter()

for word in words:
    count[word] += 1

print(count.most_common(int(input("Enter: "))))



    

