# Summarize Shop Orders by Category
# Complete the summarize_orders function.

# A fantasy game shop tracks each purchase as a dictionary with these keys:

# "item": the item name (string)
# "category": the item category (string), like "weapon" or "consumable"
# "price": the price of a single item (integer)
# "quantity": how many were bought (integer)
# All the orders are stored in a list of dictionaries.

# Your job is to summarize all orders by category.

# Function Requirements
# Write a function:

# def summarize_orders(orders):
#     # your code

# orders is a list of dictionaries (each dictionary is a single order).
# Return a new dictionary where:
# Each key is a category (string).
# Each value is another dictionary with two keys:
# "total_quantity": the sum of all quantities for that category
# "total_revenue": the sum of price * quantity for that category
# If orders is empty, return an empty dictionary {}.

# You should:

# Loop through the list of orders.
# For each order, look at its "category", "price", and "quantity".
# If the category is not in the summary dictionary yet, add it with starting values of 0.
# Update the "total_quantity" and "total_revenue" for that category.
# Example
# orders = [
#     {"item": "Health Potion", "category": "consumable", "price": 10, "quantity": 2},
#     {"item": "Mana Potion", "category": "consumable", "price": 15, "quantity": 1},
#     {"item": "Iron Sword", "category": "weapon", "price": 100, "quantity": 1},
# ]

# result = summarize_orders(orders)
# print(result)

# Expected output:

# {
#     "consumable": {
#         "total_quantity": 3,      # 2 + 1
#         "total_revenue": 35       # (2 * 10) + (1 * 15)
#     },
#     "weapon": {
#         "total_quantity": 1,      # 1
#         "total_revenue": 100      # (1 * 100)
#     }
# }

# Another example with a single category:

# orders = [
#     {"item": "Arrow", "category": "ammo", "price": 1, "quantity": 50},
#     {"item": "Fire Arrow", "category": "ammo", "price": 3, "quantity": 10},
# ]

# result = summarize_orders(orders)
# print(result)

# Expected output:

# {
#     "ammo": {
#         "total_quantity": 60,     # 50 + 10
#         "total_revenue": 80       # (50 * 1) + (10 * 3)
#     }
# }

# Focus on using dictionaries to build up this summary as you loop through the orders.

def summarize_orders(orders):
    summarized = {}

    for order in orders:
        category = order["category"]
        price = order["price"]
        quantity = order["quantity"]

        if category not in summarized:
            summarized[category] = {
                "total_quantity": 0,
                "total_revenue": 0,
            }

        summarized[category]["total_quantity"] = summarized[category]["total_quantity"] + quantity
        summarized[category]["total_revenue"] = summarized[category]["total_revenue"] + price * quantity

    return summarized