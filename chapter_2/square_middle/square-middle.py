# Write your square_middle() function here along with any subroutines that you need.
def pow_10(n):
    return 10**n

def count_num_digits(x: int) -> int:
    """
    Count the number of digits in a positive integer x.

    Parameters:
    - x (int): a positive integer

    Returns:
    int: the number of digits in x
    """

    if x == 0:
        return 1

    count = 0
    x = abs(x)
    while x > 0:
        x = x//10
        count +=1 
    return count


def square_middle(x, num_digits):
    """
    Get the middle digits of x squared.

    Parameters:
    - x (int): a positive integer
    - num_digits (int): the number of digits in the middle of x squared to return

    Returns:
    int: the middle digits of x squared
    """
    m = x**2
    current_digit_count = count_num_digits(m)

    if x<0 or num_digits<0:
        return -1
    
    if count_num_digits(x) > num_digits:
        return -1

    if num_digits % 2 == 1:
        return -1

    takeaway = (num_digits) // 2 
    first_power = num_digits + takeaway 
    intermediate = m % (pow_10(first_power))
    middle_digits = intermediate // (pow_10(takeaway))

    return middle_digits

    
