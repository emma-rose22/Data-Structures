"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

"""
#first pass 
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.insert(0, value)
        self.size += 1

    def dequeue(self):
        #removes items from queue
        self.size -= 1
        return self.storage.pop()

q = Queue()

print(q.__len__())
q.enqueue('puppies')
q.enqueue('apples')
q.enqueue('soccer ball')

print(q.__len__())
print(q.storage)

q.dequeue()
print(q.storage)

"""

#second pass 
class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value

    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None #first node in list
        #because we can only look at the beginning, we have to cycle through the whole list to get to the end
        self.tail = None

    #now we can directly add nodes to the list, no traversing
    #so now it is 0(1)
    def add_to_end(self, value):
        # what if the list is empty?
        # -- value is the actual value, not wrapped by node
        # -- wrap it in node and make it first in our list

        new_node = Node(value) # we should do this regardless if empty

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        
        # and not empty?
        else:
            #now we don't need to traverse the whole list

            #set the current tail's next to the new node
            self.tail.set_next(new_node)
            #set self.tail to the new node
            self.tail = new_node

    #we can directly remove this, no traversing
    #O(1)
    def remove_from_head(self):
        #what if the list is empty?
        # -- nothing to remove

        if not self.head:
            return None
        #what if the list isn't empty?
        else:
            #we want to return value at current head
            #also want to remove the value
            #and update self.head

            value = self.head.get_value()

            self.head = self.head.get_next()

            return value

    def add_to_head(self, value):
      new_node = Node(value)

      if not self.head and not self.tail:
        self.head = new_node
        self.tail = new_node

      else:
        new_node.set_next(self.head)
        self.head = new_node

    def print_ll_elements(self):
      current = self.head

      while current is not None:
        print(current.value)
        current = current.get_next


class Queue(LinkedList):
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        #adds items to queue
        self.storage.add_to_end(value)
        self.size += 1

    def dequeue(self):
        #removes items from queue
        if self.size > 0:
            self.size -= 1
        else:
            pass
        return self.storage.remove_from_head()

q = Queue()

print(q.__len__())
q.enqueue('puppies')
q.enqueue('apples')
q.enqueue('soccer ball')

print(q.__len__())
q.dequeue()
print(q.__len__())