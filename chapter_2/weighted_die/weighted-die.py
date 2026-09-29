import random # this should be helpful!

# Write your weighted_die() function here along with any subroutines that you need.
def weighted_die() -> int:
    """
    Simulate a weighted die that has a 10% chance of rolling a 1, a 10% chance of rolling a 2, a 50% chance of rolling a
    3, a 10% chance of rolling a 4, a 10% chance of rolling a 5, and a 10% chance of rolling a 6.

    Returns:
    int: a random integer between 1 and 6, inclusive, with the above probabilities
    """

    roll = random.randint(1, 100)

    if roll <= 10:
        return 1
    elif roll <= 20:
        return 2
    elif roll <= 70:
        return 3
    elif roll <= 80:
        return 4
    elif roll <= 90:
        return 5
    else:
        return 6

