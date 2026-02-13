# Inheritance Hierarchy
# There is no (technical) limit to how deeply we can nest an inheritance tree. For example:

# Tiger inherits from Feline inherits from Animal inherits from LivingThing.

# That said, be careful! New programmers often get carried away. You should never think to yourself:

# "Well most wizards are elves... so I'll just have Wizard inherit from Elf"

# A good child class is a strict subset of its parent class.

# Assignment
# Let's add a new game unit: Crossbowman. A crossbowman is always an archer, but not all archers are crossbowmen. Crossbowmen have several arrows, but they have an additional method: triple_shot().

# Complete the use_arrows method on the Archer class. It should remove num arrows, but if there aren't enough arrows to remove, it should raise a not enough arrows exception instead.
# Complete the Crossbowman class.
# Its constructor should call its parent's constructor.
# Its triple_shot method should:
# Use 3 arrows
# Return the string TARGET was shot by 3 crossbow bolts where TARGET is the name of the Human that was shot (any Human can be a target).

class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


## don't touch above this line


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

    def use_arrows(self, num):
        if self.__num_arrows < num:
            raise Exception(f"not enough arrows")
        self.__num_arrows -= num


class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        super().__init__(name, num_arrows)

    def triple_shot(self, target):
        self.use_arrows(3)
        target_name = target.get_name()
        return f"{target_name} was shot by 3 crossbow bolts"
    
