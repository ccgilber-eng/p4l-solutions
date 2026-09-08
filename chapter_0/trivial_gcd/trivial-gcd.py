def trivial_gcd(a: int, b: int) -> int:
    """
    Compute the greatest common divisor (GCD) of two integers using the "trivial" (brute-force) algorithm.
    Args:
        a: First integer.
        b: Second integer.
    Returns:
        The non-negative GCD of a and b. 
    """
    
    if a==0 and b!=0:
        return abs(b)

    if b==0 and a!=0:
        return abs(a)

    if a==0 and b==0:
        return 0

    d=1
    m=min(abs(a), abs(b))
    for p in range (1, m+1):
        if a%p==0 and b%p==0:
            d=p 
    return d 

# Place your min_2() subroutine here.


