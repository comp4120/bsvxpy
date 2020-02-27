#!/usr/bin/env python

from bsvxIntegerShort import IntegerShort

class IntegerLong(IntegerShort):
    def __init__(self, data, length):
        # _data is integer
        super().__init__(data)
        # _length is integer
        self._length = self.set_length(length)

    def get_length(self):
        return self._length

    def set_length(self, length):
        self._length= length
