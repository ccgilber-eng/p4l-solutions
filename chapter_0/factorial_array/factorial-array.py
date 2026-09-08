# Insert your factorial_array() function here, along with any subroutines that you need.
def factorial_array(n: int) -> list[int]:
    """
    Return a list of factorials from 0! through n!.
    Args:
        n: A non-negative integer.
    Returns:
        A list L of length n + 1 where L[k] == k! for k in [0, n].
    """
    if n<0:
        raise ValueError("Error: negative input given")

    fact=[0]*(n+1)
    fact[0]=1

    for k in range(1, n+1):
        fact[k]=fact[k-1]*k

    return fact
