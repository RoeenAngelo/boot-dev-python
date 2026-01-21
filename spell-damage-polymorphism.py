# Spell Damage Polymorphism
# Complete a small RPG-style spell system that uses polymorphism.

# You are given a base Ability class and three specific ability types:

# SwordAttack
# Fireball
# PoisonCloud
# Each ability must implement a damage(self, target_armor) method. The way damage is calculated depends on the type of ability. A function simulate_round(abilities, target_armor) should use these different implementations without caring about the concrete types – it should just call damage() on each ability.

# Your Tasks
# Implement damage for each ability class using the rules below.
# Implement simulate_round(abilities, target_armor) so that it:
# Loops through the list of abilities.
# Calls damage(target_armor) on each ability.
# Returns the sum of all damage values.
# This is where polymorphism happens: simulate_round should not check types. It should just call ability.damage(target_armor) and trust each class to do the right thing.

# Damage Rules
# All damage values must be integers. If a formula gives a negative number, return 0 instead.

# 1. Base class: Ability
# class Ability:
#     def damage(self, target_armor):
#         # you should override this in child classes
#         pass

# In the final solution, Ability.damage should be overridden by each child class. You can leave it as-is or raise an error if it’s called directly.

# 2. SwordAttack
# Constructor:

# SwordAttack(base_damage)

# Rule:

# Damage is reduced by armor.
# Formula: base_damage - target_armor, but not less than 0.
# Example:

# SwordAttack(10) vs armor 3 → 10 - 3 = 7
# SwordAttack(5) vs armor 10 → 5 - 10 = -5 → 0
# 3. Fireball
# Constructor:

# Fireball(base_damage, bonus_damage)

# Rule:

# Ignores armor completely.
# Formula: base_damage + bonus_damage.
# Example:

# Fireball(8, 4) vs armor 100 → 8 + 4 = 12
# 4. PoisonCloud
# Constructor:

# PoisonCloud(per_turn_damage, turns)

# Rules:

# Base damage: per_turn_damage * turns.
# Armor reduces the damage slightly: subtract target_armor // 2 (integer division).
# Final damage is not less than 0.
# Examples:

# PoisonCloud(3, 4) vs armor 2:

# Base = 3 * 4 = 12
# Armor reduction = 2 // 2 = 1
# Damage = 12 - 1 = 11
# PoisonCloud(2, 3) vs armor 10:

# Base = 2 * 3 = 6
# Armor reduction = 10 // 2 = 5
# Damage = 6 - 5 = 1
# simulate_round Function
# Implement:

# def simulate_round(abilities, target_armor):
#     # return the total damage dealt by all abilities
#     pass

# Behavior:

# abilities is a list of Ability objects (SwordAttack, Fireball, PoisonCloud, or any future ability type).
# For each ability in the list, call ability.damage(target_armor).
# Add up all returned damage values.
# Return the total.
# Example
# abilities = [
#     SwordAttack(10),     # vs armor 3 → 7 damage
#     Fireball(8, 4),      # ignores armor → 12 damage
# ]

# print(simulate_round(abilities, 3))
# # 19

# Another example:

# abilities = [
#     PoisonCloud(3, 4),   # base 12, armor 2 → 11 damage
# ]

# print(simulate_round(abilities, 2))
# # 11

# Summary of What You Need to Do
# Implement damage in SwordAttack, Fireball, and PoisonCloud following the rules above.
# Ensure negative damage values are turned into 0.
# Implement simulate_round(abilities, target_armor) that:
# Loops over the abilities.
# Calls the polymorphic damage method.
# Returns the total damage.
# No input or printing is required in main.py. The tests will create ability objects and call your functions directly.

class Ability:
    def damage(self, target_armor):
        pass


class SwordAttack(Ability):
    def __init__(self, base_damage):
        self.base_damage = base_damage

    def damage(self, target_armor):
        if self.base_damage - target_armor < 0:
            return 0
        return self.base_damage - target_armor



class Fireball(Ability):
    def __init__(self, base_damage, bonus_damage):
        self.base_damage = base_damage
        self.bonus_damage = bonus_damage 

    def damage(self, target_armor):
        return self.base_damage + self.bonus_damage 


class PoisonCloud(Ability):
    def __init__(self, per_turn_damage, turns):
        self.per_turn_damage = per_turn_damage
        self.turns = turns

    def damage(self, target_armor):
        if (self.per_turn_damage * self.turns) - (target_armor // 2) == 0:
            return 0
        return (self.per_turn_damage * self.turns) - (target_armor // 2)


def simulate_round(abilities, target_armor):
    damage_total = 0

    for ability in abilities:
        damage_total += ability.damage(target_armor)

    return damage_total
