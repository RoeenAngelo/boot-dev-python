# Fix Shopping Cart Class
# The ShoppingCart class is supposed to track items for each customer separately and calculate the correct total cost.

# Right now there are bugs:

# Carts for different owners share items instead of being independent.
# Adding the same item multiple times does not keep the correct quantity.
# The total cost is not always correct.
# Your job is to fix the class so that it behaves like a real shopping cart.

# Expected Behavior
# Each ShoppingCart instance represents one customer's cart.

# 1. Adding items
# Use add_item(name, price, quantity) to add items.

# If the item is not already in the cart, it should be added with the given price and quantity.
# If the item is already in the cart, its quantity should increase by the new quantity.
# For example:

# from main import ShoppingCart

# cart = ShoppingCart("Alice")

# cart.add_item("apple", 2, 3)   # 3 apples at $2 each
# cart.add_item("bread", 3, 1)   # 1 bread at $3 each
# cart.add_item("apple", 2, 2)   # 2 more apples

# # At this point the cart should contain:
# # {
# #   "apple": {"price": 2, "quantity": 5},
# #   "bread": {"price": 3, "quantity": 1}
# # }

# 2. Removing items
# Use remove_item(name) to remove an item completely from the cart.

# If the item is in the cart, it should be removed.
# If it is not in the cart, nothing should happen.
# cart.remove_item("bread")
# # Now only "apple" should remain in the cart

# 3. Getting the total cost
# Use get_total() to get the total cost of all items in the cart.

# The total is the sum of price * quantity for every item in the cart.
# If the cart is empty, the total should be 0.
# Using the example above (after adding items, before removing anything):

# total = cart.get_total()
# print(total)
# # Expected: 2 * 5 + 3 * 1 = 13

# 4. Carts must be independent
# Different ShoppingCart objects must not affect each other.

# cart1 = ShoppingCart("Alice")
# cart2 = ShoppingCart("Bob")

# cart1.add_item("potion", 5, 2)

# # cart2 should still be empty here

# If you see items from one cart showing up in another cart, something is wrong with how the cart stores its items.

# Your Task
# Fix the ShoppingCart class in main.py so that:

# Each cart keeps its own items.
# Adding the same item again increases its quantity.
# get_total() returns the sum of price * quantity for all items in that cart.
# You do not need to add new methods. Just fix the existing ones so that they behave as described.

# You can run the tests to see the current input data and how your class is behaving.

class ShoppingCart:
    

    def __init__(self, owner):
        self.owner = owner
        self.items = {}
        
    def add_item(self, name, price, quantity):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"price": price, "quantity": quantity}

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def get_total(self):
        total = 0
        for name in self.items:
            total += self.items[name]["price"] * self.items[name]["quantity"]
        return total