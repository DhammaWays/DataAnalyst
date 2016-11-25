# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 13:58:33 2016

@author: lsharma
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.pre_insert(self.root, new_val)
    
    def pre_insert(self, start, new_val):
        if( start ):
            if( new_val < start.value ):
                if( not start.left ):
                    start.left = Node(new_val)
                else:
                    self.pre_insert(start.left, new_val)
            elif( new_val > start.value ):
                if( not start.right ):
                    start.right = Node(new_val)
                else:
                    self.pre_insert(start.right, new_val)
            else: # ignoring equal value insertion
                pass
            

    def search(self, find_val):
        return self.pre_search(self.root, find_val)
        
    def pre_search(self, start, find_val):
        if( start == None ):
            return False
        elif( start.value == find_val ):
            return True
        elif( start.value < find_val ):
            return self.pre_search(start.left, find_val)
        else:
            return self.pre_search(start.right, find_val)

    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)