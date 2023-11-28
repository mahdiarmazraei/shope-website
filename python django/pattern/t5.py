class t5:
    def __init__(self):
        pass

    def sum(self,x,y):
        return x+y
    

    



class t4(t5):
    def __init__(self):
        t5.__init__(self)

x = t4()
print(x.sum(3,5))
