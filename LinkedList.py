class LinkedList:
  def __init__(self):
    self.head = None
  
  def printList(self):
    temp = self.head
    while temp:
      print(temp.data)
      temp = temp.next

  def push(self, data):
    newNode = Node(data)

    if self.head is None:
      self.head = newNode
      return
    
    last = self.head
    while last.next:
      last = last.next
    
    last.next = newNode

  def insert(self, prevNode, data):
    if prevNode is None:
      print("Error, the previous node is not inside the Linked List")
      return
    
    newNode = Node(data)

    newNode.next = prevNode.next

    prevNode.next = newNode
  
  def delete(self, data):
    temp = self.head

    if temp is not None and temp.data == data:

      self.head = temp.next
      temp = None
      return
    
    while temp is not None:
      if temp.data == data:
        break
      
      prevNode = temp
      temp = temp.next
    
    if temp is None:
      print("Could not find '" + str(data) + "' in the Linked List")
      return
    
    prevNode.next = temp.next

    del temp
  
  def deleteAt(self, position):

    if self.head == None:
      print("This list is empty!")
      return
    
    temp = self.head

    if position == 0:
      self.head = temp.next
      del temp
      return

    for i in range(position-1):
      temp = temp.next
      if temp is None:
        break
    
    if temp is None or temp.next is None:
      print("This position is out of range!")
      return
    
    next = temp.next.next

    del temp.next

    temp.next = next
  
  def length(self):
    temp = self.head
    count = 0

    while temp:
      count += 1
      temp = temp.next
    
    return count
  
  def getValue(self, index):
    temp = self.head
    
    for i in range(index):
      temp = temp.next
    
    return temp.data

  def mergeSort(self, head):

    if head is None or head.next is None:
      return head

    mid = self.getMiddle(head)
    adjacent = mid.next

    mid.next = None
    left = self.mergeSort(head)
    right = self.mergeSort(adjacent)

    sorted = self.sortedMerge(left, right)
    return sorted

  def getMiddle(self, head):
    if (head == None):
      return head
    
    slow = head
    fast = head

    while fast.next is not None and fast.next.next is not None:

      slow = slow.next
      fast = fast.next.next
    
    return slow
  
  def sortedMerge(self, first, second):

    result = None

    if first is None:
      return second
    if second is None:
      return first
    
    if first.data <= second.data:
      result = first
      result.next = self.sortedMerge(first.next, second)
    else:
      result = second
      result.next = self.sortedMerge(first, second.next)
    
    return result

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
