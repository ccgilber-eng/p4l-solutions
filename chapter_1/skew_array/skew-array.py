# Insert your skew_array() function here, along with any subroutines that you need.
def skew_array(genome: str) -> list[int]:
    """
    skew_array returns the list that represents the skew at each position of the genome. That is,       the i-th position in the list is the skew at the i-th position of the genome.
    Parameters:
    - genome (str): A genome string.
    Returns:
    - list[int]: A list representing the skew of the genome string.
    """
    if len(genome) == 0:
        raise ValueError("Error: empty genome given.")
    
    n = len(genome)

    skew_array = [0] * (n+1)

    skew: dict[str, int] = {
        "A": 0,
        "C": -1,
        "G": 1,
        "T": 0
    }

    
    for i in range(1, n+1):
        if genome[i-1] in skew:
            skew_array[i] = skew_array[i-1] + skew[genome[i-1]]
        else:
            raise ValueError("Invalid symbol given.")
    
    return skew_array
    
