class h():

    def __init__(self, matn):
        self.matn = matn


    def pr(self):
        print(self.matn)

class H():
    
    def __init__(self, h):
        print(h.matn)


x = h("hello world")
x.pr()
r = H(x)