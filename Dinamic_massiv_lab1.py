class MyList:
    def __init__(self, *data):
        self.capacity = max(len(data), 4)
        self._size = len(data)
        self._data = [None] * self.capacity
        for i in range(self._size):
            self._data[i] = data[i]
 
    def count(self):
        return self._size
 
    def get(self, index: int):
        if not 0 <= index < self._size:
            raise IndexError("Индекс вне диапазона")
        return self._data[index]
 
    def first(self):
        return self._data[0] if self._size > 0 else None
 
    def last(self):
        return self._data[self._size - 1] if self._size > 0 else None
 
    def includes(self, item):
        for i in range(self._size):
            if self._data[i] == item:
                return True, i
        return False, -1
 
    def _up_capacity(self):
        self._data.extend([None] * self.capacity)
        self.capacity *= 2
 
    def append(self, item):
        if self._size == self.capacity:
            self._up_capacity()
        self._data[self._size] = item
        self._size += 1
 
    def prepend(self, item):
        if self._size == self.capacity:
            self._up_capacity()
        self._data[1:self._size + 1] = self._data[0:self._size]
        self._data[0] = item
        self._size += 1
 
    def _remove_at(self, idx):
        del self._data[idx]
        self._data.append(None)
        self._size -= 1
 
    def remove(self, item):
        found, idx = self.includes(item)
        if found:
            self._remove_at(idx)
 
    def remove_first(self):
        if self._size > 0:
            self._remove_at(0)
 
    def remove_last(self):
        if self._size > 0:
            self._data[self._size - 1] = None
            self._size -= 1
 
    def remove_all(self):
        self._data = [None] * self.capacity
        self._size = 0
 
    def __iter__(self):
        return MyIterator(self)
 
 
class MyIterator:
    def __init__(self, iter_obj: MyList):
        self._obj = iter_obj
        self._pos = 0
 
    def first(self):
        self._pos = 0
 
    def next(self):
        self._pos += 1
 
    def is_done(self):
        return self._pos >= self._obj.count()
 
    def cur_item(self):
        if self.is_done():
            raise IndexError("Итератор закончился")
        return self._obj.get(self._pos)
 
    def __iter__(self):
        return self
 
    def __next__(self):
        if self.is_done():
            raise StopIteration
        item = self.cur_item()
        self.next()
        return item
