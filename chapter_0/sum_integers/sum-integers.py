# Insert your sum_integers() function here, along with any subroutines that you need.
def sum_integers(*numbers: int) -> int:
    """
    Return the sum of a variable number of integers.
    Args:
        numbers: Zero or more integers.
    Returns:
        The sum of all provided integers. Returns 0 if no arguments are given.
    """
    total = 0
    num_list = [*numbers]
    for val in num_list:
        total += val
    return total 
