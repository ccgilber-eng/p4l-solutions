# Insert your combination() function here, along with any subroutines that you need.
def combination(n: int, k: int) -> int:
    """
    Compute the combination statistic C(n, k) = n! / ((n - k)! * k!).
    Args:
        n: Total number of distinct objects (non-negative).
        k: Size of the subset to choose (non-negative).
    Returns:
        The number of ways to choose k items from n without order (the binomial coefficient).
    """
    if n==0 or k==0:
        return 1
    
    if n<=0 or k<=0:
        raise ValueError("Must be positive.")
    
    p = 1
    for i in range(1, n+1):
        p *= i 
    

    b = n - k
    h = 1
    for d in range (1, b+1):
        h *= d
    

    q = 1
    for x in range(1, k+1):
        q *= x
    

    return (p) // (h*q)

