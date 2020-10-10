# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# YOUR NAME

import numpy
class DynamicArray:
    pass
    
    def __init__(self):
        self.capacity = 10
        self.data = numpy.empty(self.capacity, dtype = 'O')
        self.next_index = 0

    def is_empty(self):
        return self.next_index == 0
    
    def __len__(self):
        return 0

    def append(self, item):
        self.data[self.next_index] = item
        self.next_index += 1

    def __getitem__(self, key):
        return self.data[key]
