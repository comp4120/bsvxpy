#!/usr/bin/env python

from .bsvxDataType import bsvxDataType

class Blank(bsvxDataType):
    def __init__(self):
        self._length = 0
        return
