class Node:
  def __init__(self, key=None):
    self.key = key
    self.left = None
    self.right = None

class BST:
  def __init__(self):
    self.root = None


  def findMin_ini(self):
    FNode = self.findMin(self.root)
    return FNode
  
  def findMax_ini(self):
    FNode = self.findMax(self.root)
    return FNode

  def traverseInOrder_ini(self):
    self.traverseInOrder(self.root)


  def findMin(self, root):
    while root.left is not None: #Shift over to the furthest left node to find minimum
      root = root.left
    return root


  def findMax(self, root): #Shift over to the furthest right node to find maximum
    while root.right is not None:
      root = root.right
    return root


  def insertInTree(self, root, key):
    newNode = Node(key)
    parent = None
    x = root

    while x is not None: #If the root exists
      parent = x 
      if key < x.key:
        x = x.left
      else:
        x = x.right

    if parent is None: #If a parent node does not exist
      root = newNode
    elif key < parent.key: #If the value is less than parent value, then add to left
      parent.left = newNode
    else: #Else add it to the right
      parent.right = newNode
    return root

  def delete(self, root, key):
    parent = None #Pointer that stores parent node of current node
    x = root #Current node

    while x is not None and x.key != key:
      parent = x
      if key < x.key:
        x = x.left
      else:
        x = x.right

    if x is None: #If root does not exist then return nothing
      return root

    #Case 1 if node has no children
    if x.left is None and x.right is None:
      if x != root:
        if parent.left == x:
          parent.left = None
        else:
          parent.right = None
      else: #If only the root node exists then change root to None
        root = None 
    
    #Case 2 if node has two children
    elif x.left is not None and x.right is not None:
      successor = self.findMin(x.right) #Find minimum value for successor node

      val = successor.key #Stores successor key
      self.delete(root, successor.key) #Delete the successor

      x.key = val #Change current node's key to the successor

    #Case 3 if node only has one child
    else:
      if x.left is not None: #Search for child node
        child = x.left
      else:
        child = x.right

      if x != root: #If node being deleted is not the root node
        if x == parent.left: #Set its parent to its child
          parent.left = child 
        else:
          parent.right = child 
      else: #If node being deleted IS the root node
        root = child #Set root to child
    
    return root

    
  def traverseInOrder(self, root):
    if root is None:
      return
    
    if root.left is not None:
      self.traverseInOrder(root.left)

    print(root.key, end=' ')

    if root.right is not None:
      self.traverseInOrder(root.right)


  def delete_ini(self, key):
    self.root = self.delete(self.root, key)

  def insert(self, data):
    self.root = self.insertInTree(self.root, data)

  def visit(self, node):
    print (node.key)

  def getRoot(self):
    return self.root


def main():

  print ("\nInsert the following numbers: ")
  print ("15, 23, 32, 40, 57, 36, 88")

  Tree = BST()
  Tree.insert(15)
  Tree.insert(23)
  Tree.insert(32)
  Tree.insert(40)
  Tree.insert(57)
  Tree.insert(36)
  Tree.insert(88)

  print ("Output the Min Value: ")
  min = Tree.findMin_ini()
  print (min.key, "\n")

  print ("Output the Max Value: ")
  max = Tree.findMax_ini()
  print (max.key, "\n")

  print ("Inorder traversal of the given tree: ")
  Tree.traverseInOrder_ini()

  print ("\n Now delete 40")
  Tree.delete_ini(40)

  print ("\nInorder traversal of tree")
  Tree.traverseInOrder_ini()

  print ("\n Now delete 15")
  Tree.delete_ini(15)

  print ("\nInorder traversal of tree")
  Tree.traverseInOrder_ini()

  print ("\nOutput the new root node: ")
  gt = Tree.getRoot()
  print (gt.key)

 
if __name__ == "__main__":
  main()