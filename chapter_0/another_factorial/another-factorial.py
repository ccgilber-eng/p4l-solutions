# Insert your another_factorial() function here.
def another_factorial(n: int) -> int:
    """
    Compute n! (factorial) using a for loop.
    Args:
        n: A non-negative integer.
    Returns:
        The factorial of n.
    Raises:
        ValueError: If n is negative.
    """
    if n<0:
        raise ValueError("Error: negative input given to factorial().")
    
    p=1

    for i in range(n, 0, -1):
        p=p*i

    return p 
