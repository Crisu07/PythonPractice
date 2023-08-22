import numpy as np
from base import BaseList

class DLList(BaseList):
    
    class Node(object):
        def __init__(self, x):
            self.x = x
            self.next = None
            self.prev = None

    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)


    def _initialize(self):
        self.n = 0 
        self.dummy = DLList.Node(None) 
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy


    def get_node(self, i: int) -> Node:       
        if i < (self.n / 2):
            c = 0
            temp = self.dummy.next
            while c != i: 
                temp = temp.next
                c += 1
        else:
            c = 0
            temp = self.dummy
            while c != (self.n - i): 
                temp = temp.prev
                c += 1
        return temp


    def get(self, i: int):
        if i < 0 or i >= self.n: raise IndexError()
        return self.get_node(i).x


    def set(self, i: int, x):       
        temp = self.get_node(i)
        old_value = temp.x
        temp.x = x

        return old_value

    def _remove(self, w: Node):
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1


    def remove(self, i: int):
        if i < 0 or i >= self.n: raise IndexError()
        self._remove(self.get_node(i))

    def add_before(self, w: Node, x):
        newNode = DLList.Node(x)
        newNode.prev = w.prev
        newNode.next = w
        newNode.next.prev = newNode
        newNode.prev.next = newNode
        self.n += 1
        return newNode

    def add(self, i: int, x):
        if i < 0 or i > self.n:    raise IndexError()
        self.add_before(self.get_node(i), x)

    def __iter__(self):
        u = self.dummy.next

        while u != self.dummy:
            yield u.x
            u = u.next


    def size(self) -> int:
        return self.n


    def append(self, x : np.object)  :
        self.add(self.n, x)


    def isPalindrome(self) -> bool :
        forward = self.dummy
        backward = self.dummy
        counter = 0
        check = 0

        if self.n % 2 == 0:
            while counter <= n/2: 
                if forward.next.x == backward.prev.x:
                    check += 1
                    counter += 1
                    forward = forward.next
                    backward = backward.prev
                else:
                    return False
            if check == (self.n / 2):
                return True
        else:
            while counter < ((self.n // 2) + 1): 
                if forward.next.x == backward.prev.x:
                    check += 1
                    counter += 1
                    forward = forward.next
                    backward = backward.prev
                else:
                    return False
            if check == ((self.n // 2) + 1): 
                return True

    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += " "
        return s + "]"

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
             raise StopIteration()
        return x



dl = DLList()

# | Comment out the dl.remove(0) to run the rest of the code smoothly without errors
#\/
#dl.remove(0)    # print error message or raise exception

dl.add(0,5)
print(dl)   # print [5]
dl.add(0,1)
print(dl)   # print [1,5]
dl.add(1,3)
print(dl)   # print [1,3,5]
dl.add(2,6)
print(dl)   # print [1,3,6,5]
dl.remove(2)
print(dl)   # print [1,3,5]
dl.add(1,2)
print(dl)   # print [1,2,3,5]
dl.add(3,4)
print(dl)   # print [1,2,3,4,5]
dl.append(6)
print(dl)   # print [1,2,3,4,5,6]
dl.set(5,1)
print(dl)   # print [1,2,3,4,5,1]
dl.remove(3)
print(dl)   # print [1,2,3,5,1]
print(dl.isPalindrome())    # print False
dl.set(1,5)
print(dl)   # print [1,5,3,5,1]
print(dl.isPalindrome())    # print True