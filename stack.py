import ctypes


class Stack:
    def __init__(self):
        self._array = ctypes.c_void_p * 1

        self._length = 0
        self._capacity = 1

    def push(self, value):
        if self._capacity == self._length:
            array = ctypes.c_void_p * (self._capacity * 2)
            self._array = array(
                *list(filter(lambda x: x is not None, list(self._array))),
                value)
            self._length += 1
            self._capacity *= 2
        else:
            if self._length == 0:
                self._array = (ctypes.c_void_p * self._capacity)(value)
                self._length += 1
            else:
                self._array = (ctypes.c_void_p * self._capacity)(
                    *list(filter(lambda x: x is not None, list(self._array))),
                    value)
                self._length += 1

    def is_empty(self):
        return self._length == 0

    def length(self):
        return self._length

    def peek(self):
        if self._length == 0:
            raise IndexError("Stack is empty. Cannot peek from empty stack")
        else:
            return self._array[self._length - 1]

    def pop(self):
        top = self.peek()
        array = ctypes.c_void_p * (self._capacity - 1)
        self._array = array(*list(self._array)[:-1])
        self._capacity -= 1
        self._length -= 1
        return top


