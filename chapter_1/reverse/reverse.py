# Write your reverse() function here.
def reverse(s: str) -> str:
    """
    reverse returns the given string backwards.

    Parameters:
    - s (str): The given string to reverse.

    Returns:
    - str: The reverse of s.
    """
    characters = [] 
    n = len(s) 
    for i in range(n):
        characters.append(s[n-1-i])
    
    return "".join(characters) 
