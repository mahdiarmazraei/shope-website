class Component(object):

    def __init__(self, *arg, **kwargs):
        pass

    def component_func(self):
        pass
class Child(Component):

    def __init__(self, *args, **kwargs):

        Component.__init__(self, *args, **kwargs)
        self.name = args[0]

    def component_func(self):

        print("{}".format(self.name))

class Composite(Component):

    def __init__(self, *args, **kwargs):

        Component.__init__(self, *args, **kwargs)

        self.name = args[0]

        self.children = []

    def append_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def component_func(self):

        print("{}".format(self.name))

        for i in self.children:
            i.component_func()


sub1 = Composite("submenu1")

sub11 = Child("sub_submenu11")
sub12 = Child("sub_submenu12")

sub1.append_child(sub11)
sub1.append_child(sub12)

top = Composite("top_menu")
sub2 = Child("submenu2")
top.append_child(sub1)
top.append_child(sub2)
top.component_func()