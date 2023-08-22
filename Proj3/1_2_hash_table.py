class Entry:
    def __init__(self,key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, numBuckets): # could set to (self) only and follow next comment below
        self.nBucket = numBuckets # numBuckets should be 100
        self.buckets = [None] * self.nBucket
        #self.buckets = [None for x in range(0, self.nBucket)]
    
    def simple_hash(self, key):
        # Your code here, note you should discuss the design of your simple hash function
        hash = 0
        for char in key:
            hash += ord(char) # Ord takes the string key and returns integer representing unicode character
        return hash % self.nBucket

    def double_hash(self,key, value):
        # Your code here, note you should discuss the design of your double hash function
        index = self.simple_hash(key)
        new_entry = Entry(key,value)

        if self.buckets[index] is None:
            self.buckets[index] = new_entry
        elif self.buckets[index] is not None:
            index = 7 - hash(key) % 7

            if self.buckets[index] is None:
                self.buckets[index] = new_entry
            elif self.buckets[index] is not None:
                i = 0
                while self.buckets[index] is not None:
                    index = (self.simple_hash(key) + i * (7 - hash(key) % 7)) % len(self.buckets)
                    i += 1
                self.buckets[index] = new_entry
    
    def add(self,key,value):
        """Add Function for Simple Hashing"""
        index = self.simple_hash(key)

        key_value = Entry(key,value)

        """Handling Collisions Check"""
        if self.buckets[index] is None: # If the index is empty
            self.buckets[index] = key_value # Add key value pair into table
            return True

        else:
            item = self.buckets[index]
            prev = item
            while item is not None:
                prev = item
                item = item.next
            prev.next = key_value

    def DHadd(self,key,value):
        """Add Function for Double Hashing"""
        self.double_hash(key, value) # calls the doube hash function
    
    def updateValue(self,key,value):
        """Assign the new value to key, overwriting existing value if present"""
        index = self.simple_hash(key) # Ensures that the same key is being checked
        update_entry = Entry(key,value) # Updates the new value to the same key

        if self.buckets[index] is None: # Makes sure index being updated is not empty
            print('Index empty, no values to update')
            return True
        elif self.buckets is not None:
            self.buckets[index] = update_entry
            return True
    
    def delete(self,key):
        index = self.simple_hash(key)
        
        if self.buckets[index] is None: # If value is already empty, return false
            return False
        
        elif self.buckets[index] is not None:
            self.buckets[index] = None
    
    def lookUp(self,key):
        """Find a value with a key"""
        for i in self.buckets:
            if i is not None:
                if i.key == key:
                    print('\nThe value is: '+'{}'.format(i.value))

    def print(self):
        for j in self.buckets: # Remove the if statement to print all the empty indexes as well
            if j is not None:
                print('\n['+'{}, {}'.format(j.key,j.value)+']', end=' ')
                if j.next is not None:
                    print('['+'{}, {}'.format(j.next.key,j.next.value)+']', end=' ')
                    j = j.next
        
    def DHprint(self):
        for j in self.buckets: # Remove the if statement to print all the empty indexes as well
            if j is not None: 
                print ('['+'{}, {}'.format(j.key,j.value)+']')

if __name__ == '__main__':
    """Test Cases for Simple Hash"""

    ht = HashTable(100)
    ht.add('csulb', 1)
    ht.add('csulb', 5) # Checks if it handles collision
    ht.add('CECS', 2)
    ht.add('CECS274', 3)
    ht.print() # print(ht) doesn't work for me, ht.print() works better

    ht.updateValue('CECS', 4) # Changes the value of CECS to 4 instead of 2
    ht.print()

    ht.lookUp('CECS274') # Returns the value 
    ht.delete('CECS') # Removes completely from table
    ht.print()

    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") # Separate the two outputs

    """Test Cases for Double Hash"""

    ht = HashTable(100)
    ht.DHadd('csulb', 1)
    ht.DHadd('csulb', 1) # Will add this to the a different index
    ht.DHadd('CECS', 2)
    ht.DHadd('CECS274', 3)
    ht.DHprint()

    ht.updateValue('CECS', 4) # Changes the value of CECS to 4 instead of 2
    ht.DHprint()

    ht.lookUp('CECS274') # Returns the value 
    ht.delete('CECS') # Removes completely from table
    ht.DHprint()