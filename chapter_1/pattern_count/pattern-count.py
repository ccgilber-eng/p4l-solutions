# Write your pattern_count() function here, along with any subroutines that you need.
def pattern_count(pattern: str, text: str) -> int:
    """
    pattern_count finds the number of occurences that a given substring occurs in
    a given text string. (Relies on starting_indices as a subroutine)

    Parameters:
    - pattern (str): The substring you search for in text.
    - text (str): The parent string you are using in your search.

    Returns:
    - int: The number of times that pattern occurs in text.
    """

    def starting_indices(pattern: str, text: str) -> list:
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

    k = len(pattern)
    n = len(text)

    if k == 0:
        raise ValueError("Must provide patter")
    
    if k>n:
        return 0

    return len(starting_indices(pattern, text))
    
