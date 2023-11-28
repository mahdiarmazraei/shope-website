from collections import deque
class queue:
    def __init__(self):
        self.items = deque()


    def empty(self):
        return not self.items
        # return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)


    def dequeue(self, item):
        return self.items.popleft()
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[0]
    
    def __str__(self):
        return str(self.items)
    
if __name__ == "__main__":
    pass

a = queue()
a.enqueue("link")