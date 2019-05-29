from void_array import Array
import ctypes

class Stack:
    def __init__(self):
        self._array = Array(1)
        self._length = 0

    def push(self, value):
        if len(self._array) == self._length:
            array = Array(len(self._array) * 2)
            for i in range(len(self._array)):
                array[i] = self._array[i]
            array[len(self._array)] = value
            self._array = array
            self._length += 1
        else:
            if self._length == 0:
                self._array[0] = value
                self._length += 1
            else:
                self._array[self._length] = value
                self._length += 1

    def is_empty(self):
        return self._length == 0

    def __len__(self):
        return self._length


    def peek(self):
        if self._length == 0:
            raise IndexError("Stack is empty. Cannot peek from empty stack")
        else:
            return self._array[self._length - 1]

    def pop(self):
        top = self.peek()
        if self._length * 2 == len(self._array):
            array = Array(self._length)
        else:
            array = Array(len(self._array))
        for i in range(len(self._array) - 1):
            array[i] = self._array[i]
        self._array = array
        self._length -= 1
        return top
