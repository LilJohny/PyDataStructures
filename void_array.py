import ctypes


class Array:
    def __init__(self, size):
        if size <= 0:
            raise IndexError("Array size must be greater then 0")
        self._size = size
        array_type = ctypes.py_object * size
        self._elements = array_type()
        self.clear(None)

    def __len__(self):
        return self._size

    def __getitem__(self, ind):
        if ind < 0 or ind >= len(self):
            raise IndexError("Array subscription out of range")
        return self._elements[ind]

    def __setitem__(self, ind, value):
        if ind < 0 or ind >= len(self):
            raise IndexError("Array subscription out of range")
        self._elements[ind] = value

    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        return _ArrayIterator(self._elements)


class _ArrayIterator:
    def __init__(self, array):
        self._array_ref = array
        self._ind = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self._ind < len(self._array_ref):
            item = self._array_ref[self._ind]
            self._ind += 1
            return item
        else:
            raise StopIteration
