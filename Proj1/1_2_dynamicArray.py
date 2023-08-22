from utils import new_array


class DynamicArray:

    def __init__(self):
        self.a = new_array(1) # beginning of array
        self.n = 0 # size of items within the array
        self.capacity = len(self.a) # length of the array

    def resize(self, capacity, k):
        b = new_array(capacity) # the new array which will be empty
        for i in range(self.n):
            b[i] = self.a[i] # inserts elements into the list after the index

        for i in range(k,self.n):
            b[i+1] = self.a[i] # inserts elements afer index k, 1 position over

        self.a = b # sets list b to be the original list
        self.capacity = capacity # changes capacity for each new value

    def insert(self, k, value):
        if self.n == self.capacity: # checks if items in the array exceed the capacity
            self.resize(2 * self.capacity, k) # resizes the array for values entered without shifting

        else:
            for j in range(self.n, k, -1): # shifts only if resize isn't needed
                self.a[j] = self.a[j-1]
        self.a[k] = value # new value
        self.n += 1    # increments the items within the array

    def __str__(self):
        s = "["
        for i in range(self.n):
            s += "%r" % self.a[i]
            if i < self.n - 1:
                s += ","
        s += "]"
        return s

# Test Output
dynamic_array = DynamicArray()
dynamic_array.insert(0,1)
dynamic_array.insert(0,2)
dynamic_array.insert(1,3)
dynamic_array.insert(3,5)
dynamic_array.insert(2,4)

print(dynamic_array)
