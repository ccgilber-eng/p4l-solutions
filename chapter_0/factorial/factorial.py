# Insert your factorial() function here.
def factorial(n: int) -> int:
    """
    Compute n! (factorial) using a while loop.
    Args:
        n: A non-negative integer.
    Returns:
        The factorial of n.
    """
    p=1
    i=1
    while i <= n:
        p=p*i
        i=i+1
    return p
    
