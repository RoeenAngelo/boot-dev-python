# Apply Buffs Purely
# Complete the apply_buffs function.

# You are writing a small helper for a game. Each player has base stats, and a list of temporary "buffs" that change those stats.

# apply_buffs(base_stats, buffs) should:

# Take:
# base_stats: a dictionary like {"hp": 100, "mp": 50, "attack": 20, "defense": 10}
# buffs: a list of dictionaries, for example: [{"hp": 10, "attack": 5}, {"mp": -10}]
# Return a new dictionary with all buffs applied to the base stats
# Never change base_stats or buffs (it must be a pure function)
# Make sure no stat goes below 0 (clamp at zero)
# A function is pure if:

# It always returns the same result for the same inputs
# It has no side effects (it does not change values outside the function, like its input arguments, global variables, or files)
# In this challenge, you must:

# Treat base_stats and buffs as read-only
# Build and return a new stats dictionary with the final values
# Rules for applying buffs
# Start from the values in base_stats
# For each buff in buffs, add its values to the matching keys in the stats
# If a buff has a key that is not in base_stats, ignore that key
# After all buffs are applied, if any stat is less than 0, set it to 0
# Examples
# base_stats = {"hp": 100, "mp": 50, "attack": 20, "defense": 10}
# buffs = [
#     {"hp": 10, "attack": 5},
#     {"mp": -10}
# ]

# result = apply_buffs(base_stats, buffs)

# print(result)
# # {"hp": 110, "mp": 40, "attack": 25, "defense": 10}

# print(base_stats)
# # {"hp": 100, "mp": 50, "attack": 20, "defense": 10}
# # base_stats must NOT change

# Another example, showing clamping at zero:

# base_stats = {"hp": 30, "mp": 5, "attack": 10, "defense": 2}
# buffs = [
#     {"hp": -50, "mp": -10}
# ]

# result = apply_buffs(base_stats, buffs)

# print(result)
# # {"hp": 0, "mp": 0, "attack": 10, "defense": 2}

# Your job:

# Create a new stats dictionary based on base_stats
# Loop through each buff and update the new stats
# Ignore any buff keys that are not in base_stats
# Clamp all final values so they are not less than 0
# Return the new stats dictionary without changing the inputs

def apply_buffs(base_stats, buffs):
    new_stats = base_stats.copy()

    for buff in buffs:
        for key, value in buff.items():
            if key in new_stats:
                new_stats[key] = new_stats[key] + value
                if new_stats[key] < 0:
                    new_stats[key] = 0
    return new_stats