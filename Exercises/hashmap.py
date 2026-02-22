# Hash Function
# Let's build a toy hash map in Python. In the real world, you would almost always use the built-in Python dictionary if you need a hash map. However, just using a dictionary doesn't teach us about what's going on under the hood!

# Assignment
# As it turns out, the binary search tree was overkill for profile lookups on the LockedIn website. We don't need any of the fancy ordered traversals or range queries after all - and because LockedIn is such a business failure (our CEO's words, not mine) we can store every user in memory, no need to save them to the hard drive.

# Let's build a hashmap! We'll use the strings (usernames) as keys, and map them to user objects.

# Complete the HashMap's key_to_index method. It should:

# Take a key (string) as input
# Calculate the sum of the Unicode values of all the characters in the string using Python's ord function
# Mod (%) the sum by the size of the hashmap to get an index which should be an int
# Return the index

class HashMap:
    def key_to_index(self, key):
        sum = 0
        for letter in key:
           sum += ord(letter) 
        return sum % len(self.hashmap)

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        buckets = []
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        return str(buckets)
