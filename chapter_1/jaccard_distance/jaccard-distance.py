import sys
# Please do not remove package declarations because these are used by the autograder. If you need additional packages, then you may declare them above.

# Insert your jaccard_distance() function here, along with any subroutines that you need.
def jaccard_distance(sample1: dict[str, int], sample2: dict[str, int]) -> float:
    """
    Compute the Jaccard distance between two frequency tables.

    Args:
        sample1: A frequency table mapping strings to integers.
        sample2: A frequency table mapping strings to integers.
    Returns:
        The Jaccard distance between the two samples.
    """

    a = sum_of_maxima(sample1, sample2)
    b = sum_of_minima(sample1, sample2)

    return 1 - (b / a)

    

def sum_of_maxima(sample1: dict, sample2: dict) -> int:
    """
    sum_of_maxima returns the sum of the maxima of the values for shared keys
    across two samples. If a key is not shared it is still added to the sum.

    Parameters:
    - sample1 (dict): A given input sample.
    - sample2 (dict): Another given input sample.

    Returns:
    - int: The sum of the minima of all values for shared keys.  
    If a key is not shared it is still added to the sum.
    """
    
    maxima_sum = 0

    for k in sample1:
        if k in sample2:
            maximum = max2(sample1[k], sample2[k])
            maxima_sum += maximum
        else:
            maxima_sum += sample1[k]

    for d in sample2:
        if d not in sample1: 
            maxima_sum += sample2[d]
        else:
            maxima_sum += 0

    return maxima_sum


def sum_of_minima(sample1: dict, sample2: dict) -> int:
    """
    sum_of_minima returns the sum of the minima of the values for shared keys
    across two samples.

    Parameters:
    - sample1 (dict): A given input sample.
    - sample2 (dict): Another given input sample.

    Returns:
    - int: The sum of the minima of all values for shared keys. 
    """

    total_minima_sum = 0

    for k in sample1:
        if k in sample2: 
            minimum = min2(sample1[k], sample2[k])
            total_minima_sum += minimum 
    return total_minima_sum

# Note: for the sake of convenience, we are providing min2() and max2() functions below.
def min2(x: int, y: int) -> int:
    """
    Return the minimum of two integers.

    Args:
        x: An integer.
        y: An integer.
    Returns:
        The smaller of x and y.
    """
    if x < y:
        return x
    return y

def max2(x: int, y: int) -> int:
    """
    Return the maximum of two integers.

    Args:
        x: An integer.
        y: An integer.
    Returns:
        The larger of x and y.
    """
    if x > y:
        return x
    return y
