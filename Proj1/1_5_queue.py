from utils import new_array
from base import BaseList

# The operations of pop() and append() run in o(1) time which is why the operations execute in o(1) time. o(n) only occurs when the second stack is empty which doesn't happen often
class QueueStack:

    def __init__(self):
        self.array1 = [] # stack for enqueue
        self.array2 = [] # stack for dequeue

    def enqueue (self, x):
        self.array1.append(x) # appends values to enqueue stack

    def dequeue(self):
        if len(self.array1)!=0 and len(self.array2)==0: # if enqueue stack is not empty but dequeue is
            while len(self.array1) != 0:
                array1 = self.array1.pop() # stores popped enqueue element
                self.array2.append(array1) # appened the popped element into the dequeue stack

            return (self.array2.pop()) 
        
        elif len(self.array1) == 0 and len(self.array2) == 0: # checks if both stacks are empty, to know if queue is empty
            return("Queue is empty")
            
        else:
            return (self.array2.pop())

# Test Output
queue = QueueStack()
print(queue.dequeue()) # Prints queue is empty

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue()) # Returns 1
queue.enqueue(4)
print(queue.dequeue()) # Returns 2
print(queue.dequeue()) # Returns 3
queue.enqueue(5)
print(queue.dequeue()) # Returns 4
print(queue.dequeue()) # Returns 5
print(queue.dequeue()) # Returns queue is empty