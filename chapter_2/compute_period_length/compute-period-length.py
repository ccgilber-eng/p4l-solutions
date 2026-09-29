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


def compute_period_length(a: list[int]) -> int:
    """
    Compute the period length of a list of integers.

    Parameters:
    - a: a list of integers

    Returns:
    int: the length of the period of a
    """
    
    n = len(a)

    if n<2:
        return 0

    duplicate = a[-1]
    
    for i in range(n-2, -1, -1):
        if a[i] == duplicate:
            return (n-1-i)
    return 0

