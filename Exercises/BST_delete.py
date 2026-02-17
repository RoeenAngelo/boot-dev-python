# Delete
# We also need a way to remove users from our BST if a user decides to delete their account.

# Assignment
# Implement the recursive delete method. It takes a value as an input and deletes the node with that value if it exists. Each call returns the new root of the tree (or subtree) after the deletion.

# Notice that in the test suite the delete method is called like this:

# bst = bst.delete(character)

# Check if the current node is empty (has no value). If it is, return None. This represents an empty tree or a leaf node where deletion has already occurred.
# If the value to delete is less than the current node's value:
# If there's a left child, recursively delete the value from the left subtree and update the left child reference with the result.
# Return the current node.
# If the value to delete is greater than the current node's value:
# If there's a right child, recursively delete the value from the right subtree and update the right child reference with the result.
# Return the current node.
# If the value to delete equals the current node's value, we've found the node to delete:
# If there is no right child, return the left child. This bypasses the current node, effectively deleting it.
# If there is no left child, return the right child, accomplishing the same thing.
# If there are both left and right children, we need to find the new "successor": the smallest node in the right subtree, which is the value next largest after the current node's value.
# Find the smallest node in the right subtree by walking down the current right child's left branches until reaching a node with no left child.
# Replace the current node's value with this successor's value.
# Delete the successor node from the right subtree by recursively calling delete, and update the right child reference with the result.
# Return the current node.

class BSTNode:
    def delete(self, val):
        if self.val is None:
            return None
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self

        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self

        # when val is EQUAL to self.val
        if val == self.val: #This is not needed, but better for readability
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
                
        #when self.right and self.left
        # if we choose the right side as a successor ->
        # to replace the root, we then go left to make sure -> 
        # the successor will always be smaller than the right side.
        # we do this to follow the binary tree rule where left < root < right.
        # we can also choose left, but make sure to go right after.
        
            curr = self.right
            while curr.left:
                curr = curr.left
            self.val = curr.val
            self.right = self.right.delete(curr.val) #clean-up
            return self
            
    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val
