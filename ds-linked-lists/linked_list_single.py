
# 
# Code found on "http://ls.pwd.io/2014/08/singly-and-doubly-linked-lists-in-python/"
# me: William G. K. Martin
# date: March 2015
# License: unknown


# standard imports
from __future__ import print_function




# Singly-linked list
class Node(object):
    "Basic container storing data and the next Node."
    next_node = None
    def __init__(self, data, next_node):
        self.data = data 
        self.next_node = next_node

class SingleList(object):
    "Constructor for a singly linked list."
    head = None
    tail = None

    def __repr__(self):
        out = "Showing singly linked list data:\n"
        current_node = self.head
        while current_node is not self.tail:
            out += "\t -> {0}\n".format(current_node.data)
            current_node = current_node.next_node
        else:
            out += "\t -> {0}".format(current_node.data)
        return out
            
    def append(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node
        
    def remove(self, node_value):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data == node_value: # first node (head)
                if previous_node is not None:
                    previous_node.next_node = current_node.next_node
                else:
                    self.head = current_node.next_node

            # Needed for next iteration
            previous_node = current_node
            current_node = current_node.next_node

# Testing script
if __name__ == "__main__":

    # A singly linked list of Monty Python members
    s = SingleList()
    s.append('eric')
    s.append('john')
    s.append('graham')
    s.append('terry')
    s.append('terry')
    s.append('michael')
    print(s)
    
    # The story of a sad day for Monty Python
    print("After a sad day . . . ")
    s.remove("graham")
    print(s)
    print("Graham was the most lovely old lady . . . Get the burner on.")
