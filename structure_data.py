class NodeList:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Que:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
    def put(self,data):
        n = NodeList(data)
        if self.is_empty():
            self.first = n
            self.last = n
        else:
            self.last.next = n
            self.last = n
        self.size +=1
    def is_empty(self):
        return self.first is None
    def get(self):
        if self.is_empty():
            return None
        data = self.first.data
        self.first = self.first.next
        self.size -= 1
        return data

q = Que()
for i in range(10):
    q.put(i)
print(q.is_empty())
for i in range(10):
    print(q.get())
print(q.is_empty())


class Stack:
    def __init__(self):
        self.one = None
        self._size = 0
    def push(self,data):
        n = NodeList(data)
        n.next = self.one
        self.one = n
        self._size+=1
    def pull(self):
        if self.is_empty():
            return None
        data = self.one.data
        self.one = self.one.next
        self._size -=1
        return data
    def is_empty(self):
        return self.one is None

s = Stack()
for i in range(10):
    s.push(i)
print(s.is_empty())
for i in range(10):
    print(s.pull())
print(s.is_empty())  


class Deque:
    self.first = None
    self.last = None
    self._size = 0
    def Lput (self,data):
        n = NodeList(data)
        if self.is_empty():
            self.first = n
            self.last = n
        else:
            n.next = self.first
            self.first.prev = n
            self.first = n
        self._size += 1
    def RPut(self, data):
        n = NodeList(data)
        if self.is_empty():
            self.first = n
            self.last = n
        else:
            n.prev = self.last
            self.last.next = n
            self.last = n
        self._size +=1
    def LGet(self):
        if self.is_empty():
            return None
        data = self.first.data
        if self.first == self.last:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            self.first.prev = None
        self._size -= 1
        return data
    def RGet(self):
        if self.is_empty():
            return None
        data = self.last.data
        
        if self.first == self.last:
            self.first = None
            self.last = None
        else:
            self.last = self.last.prev
            self.last.next = None
        
        self._size -= 1
        return data

    def is_empty(self):
        return self.first is None
           
