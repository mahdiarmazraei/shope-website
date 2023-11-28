class bin():
    x = "hello"
    def __init__(self,pac="hello"):
        self.x = pac
        self.y = "world"



r = bin("holo")
print(r.x)
print(r.y)