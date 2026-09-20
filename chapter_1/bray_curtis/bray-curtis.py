import sys
# Please do not remove package declarations because these are used by the autograder. If you need additional packages, then you may declare them above.

# Insert your bray_curtis_distance() function here, along with any subroutines that you need.
def  bray_curtis_distance(sample1: dict[str, int], sample2: dict[str, int]) -> float:
    """
    Compute the Bray-Curtis distance between two frequency tables.

    Args:
        sample1: A frequency table mapping strings to integers.
        sample2: A frequency table mapping strings to integers.
    Returns:
        The Bray-Curtis distance between the two samples.
    """
    a = sum_of_values(sample1)
    b = sum_of_values(sample2)
    avg = (a + b)/2
    distance = 1 - ((sum_of_minima(sample1, sample2)) / avg)
    return distance 
    

# Hint: you will probably need sum_of_minima() and sum_of_values() as subroutines.

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

def sum_of_values(sample: dict) -> int:
    """
    sum_of_values finds the sum of all the integer values in the 
    key of the dictionary.

    Parameters:
    - sample1 (dict): The sample or frequency table.

    Returns:
    - int: The sum of the keys in the given sample1.
    """

    sum = 0
    for i in sample:
        sum += sample[i]
    return sum 
    
# Note: for the sake of convenience, we are providing a min2() function below.
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
