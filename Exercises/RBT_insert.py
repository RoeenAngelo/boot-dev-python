# Red-Black Tree
# A red-black tree is a kind of binary search tree that solves the "balancing" problem. It contains a bit of extra logic to ensure that as nodes are inserted and deleted, the tree remains relatively balanced.

# Click to hide video

# How It Works
# Each node in an RB Tree stores an extra bit, called the "color": either red or black. The "color" ensures that the tree remains approximately balanced during insertions and deletions. When the tree is modified, the new tree is rearranged and repainted to restore the coloring properties that constrain how unbalanced the tree can become in the worst case.



# The "red" and "black" nomenclature is arbitrary - you could call them "red vs blue" trees (shout-out rooster teeth), or not even call it "color" at all. The important part is just that we now have two "types" of nodes and that will affect the algorithm for balancing it.

# List of Very Simple Rules
# Each node is either red or black.
# The root is black.
# All Nil leaf nodes are black.
# If a node is red, then both its children are black.
# All paths from a single node go through the same number of black nodes to reach any of its descendant Nil (black) nodes.
# Assignment
# As it turns out, we've been inserting user records into our tree with incrementing numerical IDs (pre sorted data)! The app's user lookups are starting to get really slow. Let's start implementing a Red-Black tree to speed things up.

# In a normal BST, the child nodes don't need to know about, or carry a reference to their parent. The same is not true for Red-Black trees.

# The RBNode class is already implemented for you, as well as the __init__ constructor method of the RBTree class. There's also a data member, self.nil created for you in the constructor. self.nil contains the value we'll use to designate all the nil (empty) leaf nodes, which are used for rebalancing purposes but contain no "actual" value.

# Complete the insert method. It should take a value as input and add the value as a new node in the tree if the value doesn't already exist.

# Create the new_node:
# Create a new RBNode from the given input value
# The new_node shouldn't have a parent yet
# The new_node's left and right children should be nil
# The new_node is red. (new_node.red = True)
# Find the parent of the new_node if there will be one:
# Initialize a parent variable to None
# Initialize a current variable to the root node of the tree
# While current isn't a nil node:
# Set parent to the current
# If the new_node's value is less than the current node's, set current to its own left child. If new_node's value is greater, set current to its own right child. If the values are equal, just return because this value is a duplicate.
# If you followed the steps correctly, parent will be a reference to the node that will become the parent of the new_node
# Insert the new_node by setting the parent's child:
# Set the new_node's parent to the parent we just found
# If the parent is None, we are dealing with a new root, so set the tree's root data member to the new_node
# Otherwise, compare the values of the parent and new_node and set the parent's left or right child based on the results
# We're done for now! We've really just made another (more complicated) regular binary tree, seeing as it's not a fully-fledged red-black tree yet... but these upgrades will allow us to implement the rest of the logic in the next few lessons.

# So far we've added:

# a parent pointer from child to parent (so children know who their parents are)
# the mechanisms for coloring the nodes, but have defaulted them all to red for now
# Tip
# I'd highly recommend using pencil/paper or some kind of drawing tool to visualize the tree as you go through the assignments in this chapter.

class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None) #self.nil is a special node representing “empty child”.
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil 
        new_node.right = self.nil
        new_node.red = True
        
        current = self.root
        parent = None
        
        while current is not self.nil: 
            parent = current 
            if new_node.val < current.val: 
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else: # both values are EQUAL
                return

        new_node.parent = parent 
        
        if parent is None:
            self.root = new_node
        elif new_node.val < new_node.parent.val: 
                parent.left = new_node
        else:
            parent.right = new_node