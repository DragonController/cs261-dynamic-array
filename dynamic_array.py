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
        return self.next_index

    def append(self, item):
        self.data[self.next_index] = item
        self.next_index += 1

    def __getitem__(self, key):
        if key < 0 or key >= self.next_index:
            raise(IndexError)
        return self.data[key]

    def clear(self):
        self.next_index = 0

    def pop(self):
        if self.next_index == 0:
            raise(IndexError)
        self.next_index -= 1
        return self.data[self.next_index]

    def delete(self, key):
        for index in range(key, self.next_index):
            self.data[index] = self.data[index + 1]
        self.next_index -= 1
