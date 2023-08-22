from utils import new_array
from base import BaseSet

class ArrayQueue(BaseSet):
    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)
        
    def _initialize(self):
        self.a = new_array(1) # Array[None] at the beginning of it
        self.n = 0            # the size
        self.k = len(self.a)  # Length of the array
    
    def resize (self, k):
        b = new_array(k*2) # new array but doubled in size

        for i in range(self.n): # copies the old array over to the new
            b[i] = self.a[i]

        self.a = b # updates the original array
        self.k *=2 # fixes the length
    
    def add(self, x):
        if self.n>0: # checks if the list is empty or not
            if self.k % self.n ==0: # modular arithmetic to check if it is full
                self.resize(self.k)

            self.a[self.n] = x # adds the new element
            self.n += 1 # updates the total items in list

        else:
            self.a[self.n] = x # if list is empty add item only
            self.n += 1

    def remove(self):
        if self.n == 0:
            print('Queue is empty')
          
        else: # if the list is not empty
            a = self.a[0] # stores first item
            self.a[0] = [None] # removes first item

            for y in range (0, self.n-1): # loop to shift the items back
                self.a[y] = self.a[y+1]
            self. n -= 1
            print(a)

# Test Output
queue = ArrayQueue()

queue.remove() # it prints “Queue is empty”
queue.add(1)
queue.add(2)
queue.add(3)
queue.remove() # it returns 1
queue.add(4)
queue.remove() # it returns 2
queue.remove() # it returns 3
queue.add(5)
queue.remove() # it returns 4
queue.remove() # it returns 5
queue.remove() # it prints 'Queue is empty'