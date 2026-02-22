# Get
# Now that we can insert our users and their records into our hashmap, we need a way to retrieve that information when requested!

# Assignment
# Complete the get method. It takes a key (a string) and returns the value stored at that location (not the whole key/value tuple).

# Use the key_to_index method to find the correct index to look up in the self.hashmap datastore, and if a value doesn't exist at that index, raise the following Exception to indicate no key was found.

# raise Exception("sorry, key not found")

# Due to our simple implementation, some of the keys that are inserted into the hashmap will have colliding values, which may lead to strange results - that's okay!

class HashMap:
    def get(self, key):
        index = self.key_to_index(key)

        if self.hashmap[index] is None:
            raise Exception("sorry, key not found")
        key, value = self.hashmap[index]
        return value