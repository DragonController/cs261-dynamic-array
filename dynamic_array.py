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
        if self.next_index == self.capacity:
            self.capacity *= 2
            self.data = numpy.resize(self.data, self.capacity)
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
        if key < 0 or key >= self.next_index:
            raise(IndexError)
        self.data = numpy.delete(self.data, key)
        self.next_index -= 1


    def insert(self, key, item):
        if key < 0 or key > self.next_index:
            raise(IndexError)
        self.data = numpy.insert(self.data, key, item)
        self.next_index += 1

    def is_full(self):
        return self.next_index == self.capacity

    def max(self):
        if self.next_index == 0:
            return None
        return numpy.max(numpy.resize(self.data, self.next_index))

    def min(self):
        if self.next_index == 0:
            return None
        return numpy.min(numpy.resize(self.data, self.next_index))

    def sum(self):
        if self.next_index == 0:
            return None
        return numpy.sum(numpy.resize(self.data, self.next_index))

    def linear_search(self, item):
        for index in range(self.next_index):
            if self.data[index] == item:
                return index
        return None
