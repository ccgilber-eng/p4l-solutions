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
       
    

