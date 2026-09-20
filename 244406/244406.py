import random # this should be helpful!

def monty_hall(num_trials: int, switch: bool) -> float:
    """
    Simulate the Monty Hall game show problem.

    Parameters:
        num_trials (int): The number of games to simulate.
        switch (bool): True if the contestant always switches,
                       False if the contestant always stays.

    Returns:
        float: The estimated probability of winning the prize.
    """

    wins = 0

    for i in range(num_trials):
        if switch == True:
            prize_door = random.randint(0, 2)
            choice_door = random.randint(0, 2)
            if prize_door != choice_door:
                wins += 1
            else: 
                wins += 0
        
        else:
            prize_door = random.randint(0, 2)
            choice_door = random.randint(0, 2)
            if prize_door == choice_door:
                wins += 1
            else:
                wins += 0

    
    return (wins / num_trials)


