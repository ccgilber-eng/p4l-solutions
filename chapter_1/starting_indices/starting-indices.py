 

# Insert your starting_indices() function here.
def starting_indices(pattern: str, text: str) -> list:
    """
    starting_indices returns the list containing all the starting positions of 
    pattern in text.

    Parameters:
    - pattern (str): A given substring.
    - text (str): A given superstring.

    Returns:
    - list: A list containing the starting positions of pattern in text (indices).
    """
    k = len(pattern)
    n = len(text)
    if k == 0:
        raise ValueError("Must include pattern")
    if k>n:
        return 0
    positions = []
    for i in range(n-k+1):
        if text[i:i+k] == pattern:
            positions.append(i)
            
    return positions 
