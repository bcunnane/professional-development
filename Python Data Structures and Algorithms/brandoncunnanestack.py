"""
Brandon Cunnane
CS C3 assignment 3
Stack class
"""

class Stack:
    
    def __init__(self):
        Stack.create_stack(self)
    
    def push(self, node):
        self.append(node)
    
    def pop(self):
        self.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def is_empty(self):
        return self.items == []
    
    def create_stack(self):
        self.items = []
    
    def delete_stack(self):
        self.items = []