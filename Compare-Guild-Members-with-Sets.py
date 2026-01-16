# Compare Guild Members with Sets
# Complete the compare_guild_members function.

# You are given two lists of player names:

# guild_a_members: players who joined Guild A
# guild_b_members: players who joined Guild B
# Players might appear more than once in a list (for example if the data was logged multiple times). You must treat each player as unique by name, ignoring duplicates.

# Use Python sets to analyze the two guilds and return a summary.

# Function Requirements
# Write a function:

# from typing import List, Dict

# def compare_guild_members(guild_a_members: List[str], guild_b_members: List[str]) -> Dict[str, object]:
#     # your code here

# It should return a dictionary with exactly these keys:

# "both": a list of player names that are in both guilds.
# "only_a": a list of player names that are only in Guild A.
# "only_b": a list of player names that are only in Guild B.
# "all_unique_count": how many unique player names appear in either guild.
# More details:

# Use sets to remove duplicates and to find:
# intersection (players in both guilds)
# differences (only in one guild)
# union (all unique players)
# The lists in "both", "only_a", and "only_b" must be sorted in ascending (A–Z) order.
# If no players match a category, return an empty list for that key.
# If an input list is empty, handle it normally.
# Example
# guild_a = ["alice", "bob", "carol", "alice"]
# guild_b = ["dave", "carol", "bob", "bob"]

# result = compare_guild_members(guild_a, guild_b)
# print(result)

# The result should be:

# {
#     "both": ["bob", "carol"],
#     "only_a": ["alice"],
#     "only_b": ["dave"],
#     "all_unique_count": 4,
# }

# Explanation:

# Unique in A: {"alice", "bob", "carol"}
# Unique in B: {"bob", "carol", "dave"}
# In both: {"bob", "carol"} → ["bob", "carol"]
# Only in A: {"alice"} → ["alice"]
# Only in B: {"dave"} → ["dave"]
# All unique: {"alice", "bob", "carol", "dave"} → count is 4
# Hints
# A set in Python stores unique items.

# Basic operations you may want to use:

# set_a & set_b: items in both sets (intersection)
# set_a - set_b: items in set_a but not in set_b (difference)
# set_a | set_b: items in either set (union)
# You can convert a set to a sorted list with:

# sorted_list = sorted(some_set)

# Return the dictionary with all four keys filled correctly.

import List, Dict, Any

def compare_guild_members(guild_a_members: List[str], guild_b_members: List[str]) -> Dict[str, Any]:
    set_a = set(guild_a_members)
    set_b = set(guild_b_members)    

    both = sorted(set_a & set_b)
    only_a = sorted(set_a - set_b)
    only_b = sorted(set_b - set_a)
    all_unique_count = len(set_a | set_b)

    return {
        "both": both,
        "only_a": only_a,
        "only_b": only_b,
        "all_unique_count": all_unique_count,
    }