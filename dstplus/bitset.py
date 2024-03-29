"""
This module contains impelemntation of set
suitable for integer values.

Right now it assumed that numbers are non-negative.

It is also assumed that they are not too big. Othersize
good performance is not guaranteed.
"""


class BitSet:
    """
    Implements set of non-negative integers as bitflags

    It is assumed to be API-compatible with standard Python set
    """

    def __init__(self):
        """
        Creates empty set
        """
        self.clear()

    def add(self, value):
        """
        Adds element to set
        """
        if value not in self:
            self._size += 1
        self._flags |= (1 << value)

    def remove(self, value):
        """
        Removes element from set
        """
        if value in self:
            self._size -= 1
        self._flags &= ~(1 << value)

    def clear(self):
        """
        Removes all elements from set
        """
        self._flags = 0
        self._size = 0

    def union(self, other):
        """
        Adds all elements of other set to this one
        """
        result = BitSet()
        result._flags = self._flags | other._flags
        result._size = num_of_bits(result._flags)
        return result

    def __or__(self, other):
        return self.union(other)

    def __contains__(self, value):
        return (self._flags & (1 << value)) != 0

    def __len__(self):
        return self._size


def num_of_bits(value):
    # very naive implementation
    # to be enhanced
    print("bits", value)
    result = 0
    while value:
        result += value & 1
        value >>= 1
    return result
