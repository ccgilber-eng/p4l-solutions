# Insert your euclid_gcd() function here.
def euclid_gcd(a: int, b: int) -> int:
    """
    Compute the greatest common divisor (GCD) of two integers using Euclid's algorithm.
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

    if b==0 and a==0:
        return 0 

    magnitude_b=abs(b)
    magnitude_a=abs(a)


    while magnitude_a!=magnitude_b:
        if magnitude_a>magnitude_b:
            magnitude_a=magnitude_a-magnitude_b
        else:
            magnitude_b=magnitude_b-magnitude_a

    return magnitude_a
