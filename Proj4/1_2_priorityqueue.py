class priorityQueue:
    def __init__(self):
        self.heap=[]                # an array of integers
        self.size = 0               # the size of heap

    def __len__(self):
        return self.size

    def parent(self,index):
        x = (index - 1) // 2
        return x
        
    def leftChild(self,index):
        x = (index * 2) + 1
        return x
        
    def rightChild(self,index):
        x = (index * 2) + 2
        return x
        
    def swap(self, index1, index2): #Swap the elements at indices index1 and index2 of the array
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        
    def insert(self,x): #Add value to heap and increase the length of it
        self.heap.append(x)
        self.upheap(self.size)
        self.size += 1

    def upheap(self, j): #Extra Function added
        parent = self.parent(j) #Assigns parent value
        if j > 0 and self.heap[j] > self.heap[parent]: #If index is over 0 and its value is larger than parent
            self.swap(j, parent) #Swap and recursively upheap again
            self.upheap(parent)
    
    def downheap(self, j): #2nd Extra Function added
        item = self.leftChild(j)
        item2 = self.rightChild(j)
        
        while item < self.size:
            #Case 1 if right child is smaller than the heap size and value of left child is less than right
            if item2 < self.size and self.heap[item] < self.heap[item2]: 
                item += 1 #Increase/Shift left child -> [(index*2)+1] + 1

            #Case 2 if value of left child is greater than the passed in value
            if self.heap[item] > self.heap[j]:
                self.swap(item, j) #Swap and recursively downheap again
                self.downheap(item)
            
            #Case 3 if the heap is empty, just return
            else:
                return

    def delete_Max(self):
        if self.heap is None: #If the queue is empty then return
            print ('Priority Queue is empty')
            return
        self.size -= 1
        self.swap(0, self.size)
        item = self.heap.pop()
        self.downheap(0)
        return item

       

#Test case
h = priorityQueue()
h.insert(22)
h.insert(31)
h.insert(12)
h.insert(46)
h.insert(37)
h.insert(32)
print(h.heap)
x = h.delete_Max()
print(h.heap)
x = h.delete_Max()
h.insert(66)
h.insert(42)
h.insert(56)
print(h.heap)
x = h.delete_Max()
h.insert(41)
h.insert(121)
print(h.heap)
x = h.delete_Max()
print(h.heap)
# Default outputs:
#[46, 37, 32, 22, 31, 12]
#[37, 31, 32, 22, 12]
#[66, 32, 56, 22, 31, 12, 42]
#[121, 56, 42, 32, 31, 12, 41, 22]
#[56, 32, 42, 22, 31, 12, 41]