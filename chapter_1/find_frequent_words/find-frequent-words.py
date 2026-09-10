# Insert your find_frequent_words() function here, along with any subroutines that you need.
def find_frequent_words(text: str, k: int) -> list[str]:
    """
    find_frequent_words returns a list containing the most frequent k-mers occurring in text,           including overlaps.
    Parameters:
    - text (str): A given text for the function.
    - k (int): The size of the k-mers.
    Returns:
    - The list of the most frequent k-mers occurring in text, including overlaps.
    """
    if k<=0:
        raise ValueError("Must be positive")
    if k > len(text):
        return []
    freq_patterns = []
    freq_map = frequency_table(text, k)
    max_val = max_map_value(freq_map)

    for pattern, val in freq_map.items():
        if val == max_val:
            freq_patterns.append(pattern)
            
    return freq_patterns 
