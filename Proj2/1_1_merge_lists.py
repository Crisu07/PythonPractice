class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next


class LinkedList:
  def __init__(self):  
    self.head = None
  

  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  

  # print method for the linked list
  def printLL(self):
    current = self.head
    while(current):
      print(current.data, end=" ")
      current = current.next

def merge(List_1, List_2):
    # Node for output LinkedList   
    head_ptr = temp_ptr = Node() # head_ptr will be the head node of the output list 
    
    while List_1 or List_2:
        if List_1 and (not List_2 or List_1.data <= List_2.data):
            temp_ptr.next = Node(List_1.data)
            List_1 = List_1.next

        else:
            temp_ptr.next = Node(List_2.data)
            List_2 = List_2.next

        temp_ptr = temp_ptr.next
    return head_ptr.next # return output list

# Test merge() function
# Linked List of L
L = LinkedList()
L.insert(3)
L.insert(6)
L.insert(9)
L.insert(14)
L.insert(14)
# Linked List of M
M = LinkedList()
M.insert(2)
M.insert(8)
M.insert(15)
M.insert(19)
M.insert(22)
# Merge Function
LM = LinkedList()
LM.head=merge(L.head, M.head)
LM.printLL()