# Archer Practice
# Let's practice some of these class and objects concepts a bit more.

# Assignment
# Complete the Archer class.

# Complete the constructor. It should take the following parameters in order and set them as instance properties:
# name
# health
# num_arrows
# Complete the take_hit method. It operates on the current archer instance.
# Remove one health from the current archer.
# If the archer has no health, raise the exception: {NAME} is dead where {NAME} is the archer's name.
# Finish the shoot method. It takes an Archer instance as its target input.
# If the shooter has no arrows left, raise an exception {NAME} can't shoot where {NAME} is the shooter's name.
# Otherwise, remove an arrow from the shooter.
# Print {1} shoots {2} where {1} is the shooter's name and {2} is the name of the targeted archer.
# Call the target's take_hit() method.

class Archer:
    def __init__(self, name, health, num_arrows):
        self.name = name
        self.health = health
        self.num_arrows = num_arrows

    def take_hit(self):
            self.health -= 1
            if self.health <= 0:
                raise Exception(f"{self.name} is dead")

    def shoot(self, target):
        if self.num_arrows <= 0:
            raise Exception(f"{self.name} can't shoot")
        else:
            self.num_arrows -= 1
            print(f"{self.name} shoots {target.name}")
            target.take_hit()







