"""
Brandon Cunnane
CS C3 assignment 3
Stack class
"""
from brandoncunnanenode import Node

class Stack:
    
    def __init__(self):
        # initialize stack
        self.create_stack(None)
    
    def push(self, next_node):
        # push next node onto stack
        # empty stack
        if self.head.get_data() == None:
            self.create_stack(next_node)
        # stack with 1 node
        elif self.head.get_next() == None:
            self.head.set_next(Node(next_node))
        # stack with 1+ node
        else:
            node = self.head
            while True:
                if node.get_next() == None:
                    node.set_next(Node(next_node))
                    break
                else:
                    node = node.get_next()
    
    
    def pop(self):
        # pop last node off of stack
        node_i = self.head
        node_ii = self.head.get_next()
        # stack with 1 node
        if node_ii == None:
            self.delete_stack()
            return node_i
        # stack with 1+ node
        while True:
            if node_ii.get_next() == None:
                node_i.set_next(None)
                return node_ii
            else:
                node_i, node_ii = node_ii, node_ii.next
    
    
    def peek(self):
        # peek at last node of stack
        if self.head.get_next() == None:
            print(self.head.data)
            return self.head
        else:
            node = self.head
            while True:
                if node.get_next() == None:
                    print(node.get_data())
                    return node
                else:
                    node = node.get_next()
     
        
    def is_empty(self):
        # checks if stack is empty
        if self.head.get_data() == None:
            return True
        else:
            return False
     
        
    def create_stack(self, the_head):
        self.head = Node(the_head)
    
    
    def delete_stack(self):
        self.create_stack(None)
    
    
    def print_stack(self):
        # show all nodes in stack
        node = self.head
        while True:
            print(node.get_data())
            if node.get_next() == None:
                return
            else:
                node = node.get_next()
