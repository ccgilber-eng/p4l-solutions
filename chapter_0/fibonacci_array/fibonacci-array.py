# Insert your fibonacci_array() function here, along with any subroutines that you need.
def fibonacci_array(n: int) -> list[int]:
    """
    Return an array of Fibonacci numbers from F₀ through Fₙ.
    Args:
        n: A non-negative integer.
    Returns:
        A list F of length n + 1 such that F[k] is the k-th Fibonacci number.
    """
    if n < 0:
        raise ValueError("Must be nonnegative.")
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1] 
    
    F = [1, 1]

    for i in range(2, n+1):
        a = F[-1] + F[-2] 
        F.append(a)
    return F
