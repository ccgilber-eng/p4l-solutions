import random # this should be helpful!

def roll_die() -> int:
    return random.randrange(1, 7)


def estimate_first_roll_win(num_trials: int) -> float:
    """
    Simulate num_trials games of craps and return the probability that
    the player wins immediately on the first roll (sum of dice = 7 or 11).

    Parameters:
        num_trials (int): The number of games to simulate.

    Returns:
        float: An estimated probability between 0 and 1 that the player 
               wins on the first roll.
    """

    count_win = 0
    count_lose = 0

    for i in range(num_trials):
        die_1 = roll_die()
        die_2 = roll_die()
        
        if die_1 + die_2 == 7 or die_1 + die_2 == 11:
            count_win += 1
        else:
            count_lose += 1
        probability = float(count_win / (count_lose + count_win))
        
    return probability 
        

