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
        self._flags |= (1 << value)

    def remove(self, value):
        """
        Removes element from set
        """
        self._flags &= ~(1 << value)

    def clear(self):
        """
        Removes all elements from set
        """
        self._flags = 0

    def __contains__(self, value):
        return (self._flags & (1 << value)) != 0
