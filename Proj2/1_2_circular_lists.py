class Node:    
    def __init__(self,data):    
        self.data = data;    
        self.next = None;    
     
class CreateList:    
 
    def __init__(self):    
        self.head = None
        
   
    def add(self,data):    
        if (self.head == None): # creates an empty list if there is none
            temp = Node(data)
            self.head = temp

            self.head.next = self.head
            return self.head
        
        else: # will continue to add values to that circular linked list
            temp = Node(data)
            temp.next = self.head.next

            self.head.next = temp
            self.head = temp

            return self.head
    

    #This function will print the nodes of circular linked list from the head
    def print(self):
        if (self.head == None): 
            print("List is empty") 
            return
  
        temp = self.head.next
        while temp: 
            print(temp.data, end = " ") 
            temp = temp.next
            if temp == self.head.next: 
                break


    #This function will count the nodes of circular linked list    
    def countNodes(self):    
        temp = self.head 
        result = 0

        if (self.head != None) : 
            while True : 
                temp = temp.next
                result += 1
                if (temp == self.head): 
                    break
        print("\nNode Count:", result)
        return result
        
     
class CircularLinkedList:    
    cl = CreateList();    
    #Adds data to the list    
    cl.add(4);    
    cl.add(5);    
    cl.add(7);    
    cl.add(8);    
    cl.add(12);    
    cl.add(56);   
    cl.add(85);
    cl.add(41); 
    #Displays all the nodes present in the list   
    cl.print();
    cl.countNodes();   