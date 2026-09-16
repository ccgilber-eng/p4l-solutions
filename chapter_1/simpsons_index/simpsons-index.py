import sys
# Please do not remove package declarations because these are used by the autograder. If you need additional packages, then you may declare them above.

# Insert your simpsons_index() function here, along with any subroutines that you need.
def simpsons_index(sample: dict[str, int]) -> float:
    """
    Compute Simpson's index of a frequency table.

    Args:
        sample: A frequency table mapping strings to integers.
    Returns:
        The Simpson's index of the sample.
    """

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

    
    total_simpsons_index = 0 
    total_count = sum_of_values(sample)

    for d in sample:
        m = ((sample[d])/total_count)**2
        total_simpsons_index += m 
        
    
    return total_simpsons_index




    
