import random # this should be helpful!

# Provided for you (from an earlier exercise):

def roll_die() -> int:
    """
    Simulates the roll of a die.
    Returns:
    - int: A pseudorandom integer between 1 and 6, inclusively.
    """
    return random.randrange(1, 7)
    
def sum_two_dice() -> int:
    """
    Return the sum of rolling two dice.
    """
    return roll_die() + roll_die()

def sum_dice(num_dice: int) -> int:
    total = 0
    for _ in range(num_dice):
        total += roll_die()
    return total


# Write your play_craps_once() function here along with any subroutines that you need.
def play_craps_once() -> bool:
    """
    Simulate a single game of craps and determine the outcome.

    This function simulates a single game of craps by rolling two dice.
    The outcome is determined based on the rules of craps:

    - If the first roll is 7 or 11, the player wins.
    - If the first roll is 2, 3, or 12, the player loses.
    - Otherwise, the player continues rolling until they either roll a 7 (losing)
      or match their original roll (winning).

    Returns:
    bool: True if the player wins, False if the player loses.
    """

    first_roll = sum_dice(2)
    if first_roll == 7 or first_roll == 11:
        return True
    elif first_roll == 2 or first_roll == 3 or first_roll == 12:
        return False
    else:
        while True:
            new_roll = sum_dice(2)
            if new_roll == first_roll:
                return True
            elif new_roll == 7:
                return False

        
        
