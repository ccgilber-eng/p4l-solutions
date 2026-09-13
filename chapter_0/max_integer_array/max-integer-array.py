# Insert your max_integer_array() function here, along with any subroutines that you need.
def max_integer_array(lst: list[int]) -> int:
    """
    Return the maximum integer in a non-empty list.
    Args:
        lst: A non-empty list of integers.
    Returns:
        The largest integer in lst.
    """
    if lst == []:
        raise ValueError("List cannot be empty.")
    
    current = lst[0]
    for val in lst:
        if val > current:
            current = val
            
    
    return current 

