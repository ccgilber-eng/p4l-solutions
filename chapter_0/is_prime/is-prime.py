# Insert your is_prime() function here, along with any subroutines that you need.
import math

def is_prime(p: int) -> bool:
    """
    Determine whether an integer is prime.
    Args:
        p: Integer to test (may be negative or zero).
    Returns:
        True if p is prime, False otherwise.
    """

    if p==0:
        return False
    if p==1:
        return False
    if p==2:
        return True 


    magnitude_p=abs(p)

    for k in range (2, math.isqrt(magnitude_p)+1):
        if magnitude_p%k==0:
            return False
    return True
