
class BitSet:

    def __init__(self):
        self.clear()

    def add(self, value):
        self._flags |= (1 << value)

    def remove(self, value):
        self._flags &= ~(1 << value)

    def clear(self):
        self._flags = 0

    def __contains__(self, value):
        return (self._flags & (1 << value)) != 0
