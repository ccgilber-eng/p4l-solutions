import random # this should be helpful!

def average_game_length(num_trials: int) -> float:
    """
    Simulate num_trials games of craps and estimate the average number 
    of dice rolls per game.

    Parameters:
        num_trials (int): The number of games to simulate.

    Returns:
        float: The estimated average number of dice rolls per game.
    """
    if num_trials <= 0:
        return 0.0
    
    total_rolls = 0
    for i in range(num_trials):
        die_1 = random.randrange(1, 7)
        die_2 = random.randrange(1, 7)
        roll = die_1 + die_2
        roll_count_in_game = 1
        if roll == 2 or roll == 3 or roll == 7 or roll == 11 or roll == 12:
            total_rolls += roll_count_in_game
        else:
            point = roll
            die_1 = random.randrange(1, 7)
            die_2 = random.randrange(1, 7)
            roll = die_1 + die_2
            roll_count_in_game += 1

            while roll != point and roll != 7:
                die_1 = random.randrange(1, 7)
                die_2 = random.randrange(1, 7)
                roll = die_1 + die_2
                roll_count_in_game += 1
            total_rolls += roll_count_in_game

    return total_rolls / num_trials
