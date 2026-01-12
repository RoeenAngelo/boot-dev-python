# Summarize Inventory
# Complete the summarize_inventory function.

# You are given a list of item names from a game inventory. Each time an item appears in the list, it means the player has one more of that item.

# Your job is to summarize this inventory into a list of [item_name, count] pairs.

# Rules:

# The output should be a list of lists.
# Each inner list should look like [name, count].
# name is the item name (a string).
# count is how many times that item appears in the input list.
# Keep the items in the order they first appear.
# Do not use dictionaries or sets. Use only lists and loops.
# Function details
# summarize_inventory(items)

# Input: items – a list of strings, e.g. ["potion", "potion", "elixir"]
# Output: a list of [name, count] lists.
# Examples
# Example 1:

# items = ["potion", "potion", "elixir"]
# print(summarize_inventory(items))
# # [["potion", 2], ["elixir", 1]]

# "potion" appears 2 times
# "elixir" appears 1 time
# "potion" is first in the list, so it appears first in the result
# Example 2:

# items = ["sword", "shield", "sword", "sword"]
# print(summarize_inventory(items))
# # [["sword", 3], ["shield", 1]]

# "sword" appears 3 times
# "shield" appears 1 time
# "sword" shows up first in the input, so it comes first in the output
# Example 3 (empty list):

# items = []
# print(summarize_inventory(items))
# # []

# Hints (high level)
# You can solve this with nested loops and lists:

# Create an empty list to store your summary.
# Loop over each item name in the input list.
# For each name, loop over the summary list to see if it is already there.
# If you find it, increase its count.
# If you do not find it, add a new [name, 1] pair to the summary.
# Return the summary list at the end.
# Remember: do not use dictionaries or sets – just lists and loops.

# My Solution
# def summarize_inventory(items):
#     summary = []
#     seen = []

#     for item in items:
#         if item not in seen:
#             count = items.count(item)
#             summary.append([item, count])
#             seen.append(item)
#     return summary

def summarize_inventory(items):
    summary = []

    for name in items:
        found = False

        for pair in summary:
            if pair[0] == name:
                pair[1] = pair[1] + 1
                found = True
                break

        if not found:
            summary.append([name, 1])

    return summary
