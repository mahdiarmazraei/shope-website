class Drawingone(object):

    def draw_circle(self, x, y, radius):
        print("one {} {} {}".format(x, y, radius))

class Drawingtow(object):

    def draw_circle(self, x, y, radius):
        print("tow {} {} {}".format(x, y, radius))

class Circle(object):

    def __init__(self, x, y, radius, numbering):
        self.x = x
        self.y = y
        self.radius = radius
        self.numbering = numbering

    def draw(self):

        self.numbering.draw_circle(self.x, self.y, self.radius)


cirk = Circle(0,0,3,Drawingone())
cirk.draw()

cirk2 = Circle(0, 0, 3, Drawingtow())
cirk2.draw()