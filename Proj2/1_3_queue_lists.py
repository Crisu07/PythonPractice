class Empty(Exception):
        pass

class LinkedQueue: 
    #FIFO queue implementation using a singly linked list for storage.
    class Node:

        def __init__(self, element, next):
            self.element = element
            self.next = next

    def __init__(self):
        #Create an empty queue.
        self.head = None
        self.tail = None
        self.size = 0 # number of queue elements

    def len(self):
        #Return the number of elements in the queue.
        return self.size


    def is_empty(self):
        #Return True if the queue is empty.
        return self.size == 0


    def first(self):
        #Return (but do not remove) the element at the front of the queue
        if self.is_empty():
            raise Empty('Queue is empty') # raise empty if there is nothing in the queue
        print("First element:",self.head.element) 
        return self.head.element # the front is aligned with the head of the list



    def dequeue(self):
        #Remove and return the first element of the queue (i.e., FIFO).
        if self.is_empty():
            print('Queue is empty')
        else:
            answer = self.head.element
            self.head = self.head.next
            self.size -= 1
            if self.is_empty():
                self.tail = None
            print("Dequeued:", answer)
            return answer


    def enqueue(self, e):
        #Add an element to the back of queue
        newest = self.Node(e, None)
        if self.is_empty():
            self.head = newest
        else:
            self.tail.next = newest
        self.tail = newest
        self.size += 1




    def rotate(self):
        #Rotate front element to the back of the queue
        if self.size > 0:
            self.tail = self.tail.next
        self.tail = self.head
        self.head = self.tail.next
        self.head.next.next = self.tail # makes sure rotate repeats without errors 


queue = LinkedQueue()
queue.dequeue() # print error message or throw exception
queue.enqueue(6) # queue = 6
queue.enqueue(2) # queue = 6->2
queue.enqueue(7) # queue = 6->2->7
queue.dequeue() # print 6 and queue = 2->7
queue.first() # print 2 and queue = 2->7
queue.enqueue(1) # queue = 2->7->1
queue.rotate() # queue = 7->1->2
queue.enqueue(5) # queue = 7->1->2->5