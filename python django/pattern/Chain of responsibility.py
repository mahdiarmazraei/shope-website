class Handler:

    def __init__(self, successor):
        self.successor = successor

    def handle(self, request):
        handled = self._handle(request)

        if not handled:
            self.successor.handle(request)