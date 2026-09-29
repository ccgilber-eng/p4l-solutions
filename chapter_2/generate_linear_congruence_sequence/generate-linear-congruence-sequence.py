# Write your has_repeat() function here along with any subroutines that you need
def has_repeat(a: list[int]) -> bool:
    """
    Check if a list has repeat elements.

    Parameters:
    - a: a list of integers

    Returns:
    bool: True if a has repeat elements, False otherwise
    """
    
    read_values = []
    for val in a:
        if val in read_values:
            return True
            break 
        else: 
            read_values.append(val) 
    return False
       
    

def generate_linear_congruence_sequence(seed: int, a: int, c: int, m: int) -> list[int]:
    """
    Generate a linear congruence sequence.

    Parameters:
    - seed (int): the first value in the sequence
    - a (int): the multiplier
    - c (int): the increment
    - m (int): the modulus

    Returns:
    list: a sequence of integers produced by the linear congruential generator
    """
    sequence = []
    sequence.append(seed)
    while has_repeat(sequence) == False:
        seed = ((a*seed)+c) % m 
        sequence.append(seed)
    return sequence 
