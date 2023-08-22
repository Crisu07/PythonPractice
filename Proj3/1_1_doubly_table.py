class Node:
    def __init__(self,key,val):
        self.value = val
        self.next = None
        self.prev = None
        self.key = key
        self.index = 0
        
class HashTable:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_before(self, item:Node, key, val):
        newNode = Node(key,val)
        newNode.prev = item.prev
        newNode.next = item
        newNode.next.prev = newNode
        newNode.prev.next = newNode
        return newNode
    
    def insert_by_Index(self,index,key,val):
        if index == self.head.index: # If index is 0, insert at the head
            element = self.insert_at_First(key,val)
            return element
        elif index == self.tail.index: # If index is the tail, insert at the end
            self.insert_at_Last(key,val) 
        else:
            item = self.head
            while item.index is not index:
                item = item.next
            element = self.add_before(item,key,val)
            element.index = index

            next_item = element.next
            while next_item is not None: # Adjusts the index forward
                next_item.index += 1
                next_item = next_item.next
            
            return element
              
    def getValue_by_Index(self,index):
        element = self.head
        while element.index is not index: # Iterates through list and returns corresponding value
            element = element.next
        return element.value
                
    def getValue_by_Key(self,key):
        element = self.head
        while element.key is not key: # Similar to get value by index but this time, gets the value by the key
            element = element.next
        return element.value
        
    def delete_by_Value(self,val):
        if self.head.value == val: # Delete first value
            item=self.head
            self.head = self.head.next 
            self.head.prev = None

            newitem = item.next
            while newitem is not None: # Adjuts the index
                newitem.index -= 1
                newitem = newitem.next

        elif self.tail.value == val: # Delete the last value, no adjust index because it is at the end
            self.tail = self.tail.prev
            self.tail.next = None
            
        else:
            item = self.head.next
            newitem = item.next
            while newitem is not None: # Adjusts index again
                newitem.index -= 1
                newitem = newitem.next

            while item.value != val: # If no value exists to delete, return error
                item = item.next
                if item is None:
                    raise ValueError()

            item.prev.next = item.next
            item.next.prev = item.prev

            newitem = item.next
            while newitem is not None:
                newitem.index -= 1
                newitem = newitem.next
    
    def delete_by_Index(self,index):  # Similar to delete by value, but works with index this time
        if self.head.index == index: # If at idex 0, shift head to next index and delete the previous
            item=self.head
            self.head = self.head.next
            self.head.prev = None

            newitem = item.next
            while newitem is not None:
                newitem.index -= 1
                newitem = newitem.next
        elif index == self.tail.index: # If index is at the end, adjust tail to the one before it and delete
            self.tail = self.tail.prev
            self.tail.next = None
        elif index < self.head.index or index >= self.tail.index: # If outside of hash table range, return error
            raise IndexError()
        else:
            item = self.head
            while item.index is not index:
                item = item.next
            item.prev.next = item.next
            item.next.prev = item.prev

            newitem = item.next
            while newitem is not None: # -1 Adjusts the index back
                newitem.index -= 1
                newitem = newitem.next
     
    def delete_by_Key(self,key): # Similar to delete by index function but uses the key this time
        if self.head.key == key:
            item=self.head
            self.head = self.head.next # Removes first value found
            self.head.prev = None

            newitem = item.next
            while newitem is not None: # Fix/Adjust the index
                newitem.index -= 1
                newitem = newitem.next

        elif self.tail.key == key:
            self.tail = self.tail.prev
            self.tail.next = None
        else: # Similar to previous delete by index function
            item = self.head.next
            while item.key != key:
                item = item.next
                if item is None:
                    raise ValueError()
            item.prev.next = item.next
            item.next.prev = item.prev

            newitem = item.next
            while newitem is not None: # Readjusts index back
                newitem.index -= 1
                newitem = newitem.next
    
    def print_all_keyValues(self):
        item = self.head
        while item is not None:
            print ('{'+'{}:{}'.format(item.key,item.value)+'}')
            item = item.next

    def insert_at_First(self,key,val):
        element = Node(key,val)
        if self.head is None:
            self.head = element
            self.tail = element
            return element
        element.next = self.head
        self.head.prev = element
        self.head = element
 
        newitem = element.next
        while newitem is not None: # Adjusts the index forward
            newitem.index += 1
            newitem = newitem.next
        return element
            
    def insert_at_Last(self,key,val):
        element = Node(key,val)
        if self.head is not None: # Similar to insert at first but this time fixes the tail
            self.tail.next = element
            element.prev = self.tail
            self.tail = element
        else:
            self.head = element
            self.tail = element

        newitem = self.head.next
        while newitem is not None: # Adjusts the index again
            newitem.index = newitem.prev.index+1
            newitem = newitem.next     
    

    def length(self):
        if self.head != None and self.tail != None:
            return self.tail.index + 1
        else:
            return "Note: Table is Empty!"



# test cases               
d1 = HashTable()

d1.insert_at_First("csulb",1)
d1.insert_at_First("CECS",2)
d1.insert_at_First("CECS274",3)
d1.insert_at_Last("CS",4)

d1.insert_by_Index(1,"life",12)
d1.insert_by_Index(0,"time",44)
d1.insert_by_Index(3,"value",12)
d1.insert_by_Index(4,"good",26)
d1.insert_by_Index(4,"eng",27)

#d1.delete_by_Value(8) #will provide an error, comment out to make code run
d1.delete_by_Index(1)
d1.delete_by_Key("time")

d1.insert_at_First("why",24)
d1.insert_at_Last("how",57)
d1.insert_by_Index(3,"know",145)
d1.insert_by_Index(4,"yes",243)



print("HashTable: ",end="\n")
d1.print_all_keyValues()
print("\nLength:",d1.length())
print("Value at Key 'eng':",d1.getValue_by_Key("eng"))
print("Value at Key 'csulb':",d1.getValue_by_Key("csulb"))
print("Value at index 3:",d1.getValue_by_Index(3))
print("Value at index 7:",d1.getValue_by_Index(7))





