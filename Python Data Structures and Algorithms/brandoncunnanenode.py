"""
Brandon Cunnane
CS C3 assignment 3
Node Class
"""

class Node:
    def __init__(self,init_data):
        self.data = init_data
        self.next = None
    
    # setters
    def set_data(self,new_data):
        self.data = new_data
    
    def set_next(self,new_next):
        self.next = new_next
    
    # getters
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    # helpers
    def points_to_node(self):
        # check if node points to another node
        return isinstance(self.get_next(), Node)