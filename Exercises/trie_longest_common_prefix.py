# Longest Common Prefix
# Let's use our Trie to find the longest common prefix of a list of words. This feature can be used in LockedIn to display suggestions when users are searching for their connections.

# Assignment
# Complete the longest_common_prefix method. It returns the longest common prefix among the words in the trie.

# Initialize a variable current that references the root of the trie
# Initialize a variable prefix to an empty string
# Enter a forever while loop:
# Get the "children" (keys) in the current dictionary
# If a child is an end_symbol, break the loop.
# If there is only one child, append the character to the prefix string and update the current dictionary to point to the child dictionary corresponding to the character.
# If there are multiple children or no children, break the loop.
# Return the prefix string.
# Tips
# You can access just the keys of a dictionary with the .keys() method.
# Here's the syntax for an intentional infinite loop. Always remember to include an exit condition so it doesn't actually continue forever.
# while True:
#     if exit_condition == True:
#         break

class Trie:
    def longest_common_prefix(self):
        current = self.root
        prefix = ""
        while True:
            children = []
            for key in current.keys():
                if key == self.end_symbol:
                    break
                children.append(key)
            if len(children) == 1:
                prefix += children[0]
                current = current[children[0]]
            else:
                break
        return prefix