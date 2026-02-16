# Min and Max
# Some of the simpler BST algorithms are the get_min and get_max methods.

# Assignment
# Now that we can add users to our BST, our systems team wants us to start implementing search functionality.

# Implement the get_min and get_max methods. They should return the minimum and maximum values in the BST respectively.

# Tips
# The get_min function loops through all the left child nodes and returns the value of the last one.
# The get_max function does the same for the right children.

class BSTNode:
    def get_min(self):
        curr = self
        while curr.left:
            curr = curr.left
        return curr.val

    def get_max(self):
        curr = self
        while curr.right:
            curr = curr.right
        return curr.val
