# Rotation
# "Rotations" are what actually keep a red-black tree balanced. Every time one branch of the tree starts to get too long, we will "rotate" those branches to keep the tree shallow. A shallow tree is a healthy (fast) tree!

# A properly-ordered tree pre-rotation remains a properly-ordered tree post-rotation
# Rotations are O(1) operations
# When rotating left:
# The "pivot" node's initial parent becomes its left child
# The "pivot" node's old left child becomes its initial parent's new right child
# Here's the process of a "left rotation":



# Assignment
# Now that we can add users to our new Red Black Tree, we need to add the rotation functionality that will keep it balanced and running fast!

# Use the exact same variables as specified in the instructions. For example, pivot_parent and pivot.parent are not interchangeable as they hold state that changes throughout the algorithm's steps.

# Complete the rotate_left method. It takes a single node, pivot_parent, as input and rotates the tree with its pivot node — which in this case is its right child.
# If pivot_parent is nil or pivot_parent's right child is nil, return. Nothing to do here.
# Let pivot be pivot_parent's right child.
# Set pivot_parent's right child to be pivot's left child.
# If pivot's left child isn't a nil leaf node, set pivot's left child's parent to pivot_parent.
# Set pivot's parent to pivot_parent's parent.
# If pivot_parent is the root, set the root to pivot.
# Otherwise, if pivot_parent is its parent's left child, set pivot_parent's parent's left child to pivot.
# Otherwise, if pivot_parent is its parent's right child, set pivot_parent's parent's right child to pivot.
# Set pivot's left child to be pivot_parent.
# Set pivot_parent's parent to be pivot.
# Complete the rotate_right method with all the directionality inverted.



class RBNode:
    def __init__(self, val):
            self.red = False
            self.parent = None
            self.val = val
            self.left = None
            self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def rotate_left(self, pivot_parent):
        if pivot_parent is self.nil or pivot_parent.right is self.nil:
            return
        pivot = pivot_parent.right
        pivot_parent.right = pivot.left
        
        if pivot.left is not self.nil:
            pivot.left.parent = pivot_parent
        pivot.parent = pivot_parent.parent

        if pivot_parent == self.root:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot
        else:
            pivot.parent.right = pivot
        pivot.left = pivot_parent
        pivot_parent.parent = pivot
            

    def rotate_right(self, pivot_parent):
        if pivot_parent is self.nil or pivot_parent.left is self.nil:
            return
        pivot = pivot_parent.left
        pivot_parent.left = pivot.right
        
        if pivot.right is not self.nil:
            pivot.right.parent = pivot_parent
        pivot.parent = pivot_parent.parent

        if pivot_parent == self.root:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right = pivot
        else:
            pivot.parent.left = pivot
        pivot.right = pivot_parent
        pivot_parent.parent = pivot