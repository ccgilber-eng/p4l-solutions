import math
import random # this should be helpful!

# Write your sum_dice() function here along with any subroutines that you need.
def sum_dice(num_dice : int) -> int:
    """
    Simulate the roll of num_dice dice.

    Returns:
    int: The sum of num_dice pseudorandom integers between 1 and 6 inclusively.
    """

    def roll_die() -> int:
        return random.randrange(1, 7)

    total = 0
    for _ in range(num_dice):
        total += roll_die()
    return total

