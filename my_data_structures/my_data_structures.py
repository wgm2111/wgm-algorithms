
# 
# William GK Martin
# March 2015
# 


"""
Module containing my implementations of some basic data structures:
  Node
  LinkedList
  Stack
  Queue

"""


# My Basic singly-conected data container
class Node(object):
    """
    Basic data container with one connection to the next node.
    """
    # Class data
    data = None
    next_node = None

    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node
        
# A linked list of signly-conected nodes
class LinkedList(object):
    """
    Construct a list of singly connected nodes.
    """
    # List data
    first = None
    last = None

    # Insertion methods
    def insertFirst(self, data):
        """
        Modify the list by insertion at the first location.
        """
        if self.first is None:
            self.first = self.last = Node(data, None)
        else:
            self.first = Node(data, self.first)

    def insertLast(self, data):
        """
        Modify the list by insertion at the last location.
        """
        if self.last is None:
            self.first = self.last = Node(data, None)
        else:
            self.last.next_node = Node(data, None)
            self.last = self.last.next_node
            
    # Data retrieval methods
    def getFirst(self):
        """
        Return data from the first node.
        """
        data = None if (self.first is None) else self.first.data
        return data


    # Removal methods
    def removeFirst(self):
        """
        Remove the first Node in the list.
        """
        if self.first is self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next_node

# Implementing a stack based on the Linked list above
class Stack(LinkedList):
    """
    Construct a stack with pust/pop functionality.

    example:
    >>> s = Stack()
    >>> a = [s.push(i) for i in range(5)]
    >>> [s.pop() for i in range(6)]
    [4, 3, 2, 1, 0, None]
    """
    # Insertion methods
    def push(self, data):
        "Add data to the top."
        self.insertFirst(data)
    # Removal methods
    def pop(self):
        "Return data from the first node (and remove)."
        out = self.getFirst()
        self.removeFirst()
        return out

# Implementing a queue based on the linked list
class Queue(LinkedList):
    """
    Construct a queue with enqueue/dequeue functionality.
    >>> q = Queue()
    >>> a = [q.enqueue(i) for i in range(5)]
    >>> [q.dequeue() for i in range(6)]
    [0, 1, 2, 3, 4, None]
    """
    # Insertion methods
    def enqueue(self, data):
        "Add data to the queue at the end of the list."
        self.insertLast(data)
    # Removal methods
    def dequeue(self):
        "Return the data from the first Node and remove the node."
        out = self.getFirst()
        self.removeFirst()
        return out
        
        


# Run doctests when called as a script
if __name__ == "__main__":

    # Run the doctests
    import doctest
    doctest.testmod()
