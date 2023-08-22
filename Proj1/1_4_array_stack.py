from utils import new_array
from base import BaseList

class ArrayStack(BaseList):
    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)
        
    def _initialize(self):
        self.a = new_array(1)
        self.n = 0

    def get(self, i):
        if i < 0 or i >= self.n: raise IndexError()

        return self.a[i] # gives the target element

    def set(self, i, x):
        if i < 0 or i >= self.n: raise IndexError()

        b = self.a[i]
        self.a[i] = x # changes the old element
        return b # returns the new

    def add(self, i, x): 
        if i < 0 or i > self.n: raise IndexError()

        if self.n == len(self.a): # checks if list exceeds the size
            self._resize() 

        self.a[i+1:self.n+1] = self.a[i:self.n] # repositions the elements after the index
        self.a[i] = x # adds new element into target index
        self.n += 1 # increments elements 

    def remove(self, i): 
        if i < 0 or i >= self.n: raise IndexError()

        x = self.a[i] # stores the element that was removed
        self.a[i:self.n-1] = self.a[i+1:self.n] # shift elements back one index
        self.n -= 1 # decreases the number of elements by 1 to accomodate for the removed element

        if len(self.a) >= 3*self.n: 
            self._resize()
        return x
  
    def _resize(self):
        b = new_array(max(1, 2*self.n)) # resizes only if n is > 0

        b[0:self.n] = self.a[0:self.n] # resizes
        self.a = b # sets new array to original

# Test Output
stack = ArrayStack()
stack.add(0,1)
stack.add(0,2)
stack.add(1,3)
stack.add(3,5)
stack.add(2,4)
print(stack.get(0)) # it prints 2
print(stack.get(1)) # it prints 3
print(stack.get(2)) # it prints 4
print(stack.get(3)) # it prints 1
print(stack.get(4)) # it prints 5