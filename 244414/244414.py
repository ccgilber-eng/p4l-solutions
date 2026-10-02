import random

def dice_outcome_matrix(trials: int, seed: int) -> list[list[int]]:
    """
    Simulate rolling two fair six-sided dice `trials` times and return a 6×6 matrix
    of counts. Entry [i][j] is the number of times die1 showed (i+1) and die2 showed (j+1).

    Parameters:
        trials (int): The number of dice rolls to simulate (≥ 1).
        seed (int): random seed for reproducibility.

    Returns:
        list[list[int]]: A 6×6 matrix of counts.
    """

    matrix = [[0]*6 for k in range(6)]
    random.seed(seed) 
    for d in range(trials):
        die1 = random.randrange(1,7)
        die2 = random.randrange(1,7)
        matrix[die1-1][die2-1] += 1
    return matrix 






