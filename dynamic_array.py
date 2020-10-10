# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# YOUR NAME

import numpy
class DynamicArray:
    pass
    
    def __init__(self):
        self.capacity = 10
        self.data = numpy.full(self.capacity, object)

    def is_empty(self):
        return 1
    
    def __len__(self):
        return 0

    def append(self, item):
        self.data = numpy.full(1, item)

    def __getitem__(self, key):
        return 42
