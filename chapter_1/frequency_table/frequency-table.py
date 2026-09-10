# Insert your frequency_table() function here, along with any subroutines that you need.
def frequency_table(text: str, k: int) -> dict:
    """
    frequency_table finds the frequencies of each k-mer occuring in a given text, 
    including overlaps.

    Parameters:
    - text (str): The string text to search for kmers.
    - k (int): The size of the kmers.

    Returns:
    - dict (str : int): The dictionary of kmers to their frequencies in the given
    text string, including overlaps.
    """
    if k <= 0:
        raise ValueError("Must be positive")
    if k>len(text):
        return {}
    freq_map: dict[str, float] = {}
    n=len(text)

    for i in range(n-k+1):
        pattern = text[i:i+k]
        freq_map[pattern] = freq_map.get(pattern, 0) + 1
    return freq_map
