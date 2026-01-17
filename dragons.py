# Dragons
# In "Age of Dragons" there are Orcs, Humans, Goblins, Dragons, etc. All of those different creatures are called "units". The only thing specific to a unit is that it has a position on the game map (x and y coordinates) and a name.

# Dragons are a specific type of unit. They can breathe fire in a large area dealing damage to any units touched by its fiery blaze.

# The Game Grid
# Our game map is just a Cartesian plane.

# The example above uses a __fire_range of 1 centered at (1, 1).

# Assignment
# Complete the following methods:

# Complete the unit's in_area method. It accepts an "area" represented by four coordinates: x_1, y_1, x_2, and y_2. The coordinates x_1 and y_1 represent the bottom-left corner, while x_2 and y_2 represent the top-right corner.
# Determine if the unit is within the given area by using the unit's position coordinates pos_x and pos_y.
# Return True if the unit's position falls inside or on the edge of the rectangle. Otherwise, return False.
# Complete the dragon's breathe_fire method. It causes the dragon to breathe a swath of fire at the target area.
# The target area is centered at (x, y). The area stretches for __fire_range in both directions inclusively.
# Iterate over each unit in the units list, and check if the unit is in the area. If it is, add it to a new list that keeps track of the units hit by the blast.
# Return the list of units hit by the blast.

class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        is_within_x = x_1 <= self.pos_x <= x_2
        is_within_y = y_1 <= self.pos_y <= y_2
        return is_within_x and is_within_y


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        hit_units = []
        x1 = x - self.__fire_range
        x2 = x + self.__fire_range
        y1 = y - self.__fire_range
        y2 = y + self.__fire_range
        
        for unit in units:
            if unit.in_area(x1, y1, x2, y2):
                hit_units.append(unit)
        return hit_units
