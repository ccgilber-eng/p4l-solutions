import random # this should be helpful!

def roll_die() -> int:
    """
    Simulates the roll of a die.
    Returns:
    - int: A pseudorandom integer between 1 and 6, inclusively.
    """
    return random.randrange(1, 7)
    
def sum_dice(num_dice: int) -> int:
    """
    Simulates the process of summing n dice.
    Parameters:
    - num_dice (int): The number of dice to sum.
    Returns:
    - int: The sum of num_dice simulated dice.
    """
    total = 0
    for _ in range(num_dice):
        total += roll_die()
    return total

def play_craps_once() -> bool:
    """
    Simulates one game of craps.
    Returns:
    - bool: True if the game is a win, False if it's a loss.
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


def compute_craps_house_edge(num_trials: int) -> float:
    """
    Estimate the house edge of craps based on simulations.

    This function simulates the specified number of craps games and calculates the
    average money won or lost over those games to estimate the house edge.

    Parameters:
    - num_trials (int): The number of simulated games to play.

    Returns:
    float: The estimated house edge, representing the average money won or lost per game.
    """
    if num_trials <= 0:
        raise ValueError("num_trials must be a positive integer.")
    count = 0
    for _ in range(num_trials):
        outcome = play_craps_once()
        if outcome:
            count += 1  
        else:
            count -= 1  
    return count / num_trials   

