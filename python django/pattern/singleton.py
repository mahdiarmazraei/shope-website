class Borg:


    _shared_data = {}

    def __init__(self):
        self.__dict__ = self._shared_data


class Singleton(Borg):

    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(kwargs)


b = {'name': 'ali', 'description': 'good'}
# b2 = {'name': 'reza', 'description': 'bed'}
b2 = {"beautiful": True, "angry": True}
a = Singleton(**b)
print(a)
print(a._shared_data)

a2 = Singleton(**b2)

print(a2)
print(a2._shared_data)