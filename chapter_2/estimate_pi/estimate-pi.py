import random # this should be helpful!

# Write your estimate_pi() function here along with any subroutines that you need.
def estimate_pi(num_points: int) -> float:
    """
    Estimate pi using a Monte Carlo method.

    Parameters:
    - num_points (int): the number of points to use in the Monte Carlo method

    Returns:
    float: an estimate of pi
    """

    count = 0
    for i in range(num_points):
        a = random.uniform(-1,1)
        b = random.uniform(-1,1)
        if ((a**2)+(b**2))<=1:
            count +=1 

    
    probability = count / num_points
    return (4*probability)

