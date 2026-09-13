# Insert your list_mersenne_primes() function here, along with any subroutines that you need.
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

def list_mersenne_primes(n: int) -> list[int]:
    """
    List all Mersenne primes of the form 2^p - 1 with p ≤ n.
    Args:
        n: Upper bound on the exponent p (non-negative integer).
    Returns:
        A list of all primes of the form 2^p - 1 where p is prime and p ≤ n,
        in increasing order of p.
    """

    mersenne_list = []

    if n<=0:
        raise ValueError("Must input positive number.")
    
    p=0
    for p in range(1,n+1):
        m_p = (2**p)-1
        if is_prime(m_p) == True:
            mersenne_list.append(m_p)
    return mersenne_list 


            
