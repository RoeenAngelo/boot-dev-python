# Insert Nodes
# The building blocks of a BST are Nodes. In our implementation, we will only use a single class, the BSTNode class. Any BSTNode is technically also a full Binary Search Tree, with itself as the root node (it's not aware of any potential parents). Most of the methods that traverse the tree will do so recursively... have fun!

# Our LockedIn BSTNode
# Throughout this chapter we'll be building a binary search tree to power LockedIn's custom database. LockedIn's management doesn't trust so called "open-source"... so here we are. One of the primary features of databases is the ability to look up records by a single key, and binary search trees are the most common way to implement these fast lookups.

# Each node in our BST will represent a LockedIn user. A BSTNode has three properties:

# value: The value of the node, a User object in our case (see user.py). You'll notice that Users have a name and an ID. Comparison operators are already implemented for you on the class, so you should be able to compare User objects with ==, <, and > directly. The ID is the value that we'll use to determine the order of the nodes in the tree.
# left: The left child of the node, another BSTNode or None
# right: The right child of the node, another BSTNode or None
# Assignment
# Complete the insert method of the BSTNode class. It takes a User object as input and adds it to a new node if the value doesn't already exist in the tree.

# If the node doesn't have a value yet, just use the given value and be done
# If the node's value is equal to the given value, just be done, no duplicates allowed
# If the given value is less than the node's value and the node doesn't have a left child, create a new left child node with the given value
# If the given value is less than the node's value and the node does have a left child, recursively call insert off of that left child with the given value
# Since we already checked if the given value is equal to or less than the node, the value must be greater than the node. Handle whether or not the node already has a right child
# Tip
# I'd highly recommend using pencil/paper or some kind of drawing tool to visualize the tree as you go through the assignments in this chapter.

class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
    
    def insert(self, val):
        if self.val is None:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BSTNode(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BSTNode(val)