# Insert your permutation() function here, along with any subroutines that you need.
def permutation(n: int, k: int) -> int:
    """
    Compute the permutation statistic P(n, k) = n · (n-1) · ... · (n-k+1) = n! / (n-k)!.
    Args:
        n: Total number of distinct objects (non-negative).
        k: Number of positions to fill (non-negative).
    Returns:
        The number of ways to choose and order k items from n, i.e., P(n, k).
    """
    if n == 0 or k == 0:
        return 1

    if n <= 0 or k <= 0:
        raise ValueError("Must be positive.")
    
    p = 1
    for i in range(1, n+1):
        p *= i

    q = 1
    h = n-k

    for d in range(1, h+1):
        q *= d

    return p//q
