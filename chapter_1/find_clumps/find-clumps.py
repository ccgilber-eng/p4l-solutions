# Insert your find_clumps() function here, along with any subroutines that you need.
def find_clumps(text: str, k: int, window_length: int, t: int) -> list[str]:
    """
    Finds a list of strings representing all k-mers that appear at least t times in a window of         given length in the string.
    Parameters:
    - text (str): An input string.
    - k (int): k-mer's of size k.
    - window_length (int): the size of substrings of text in which we are looking for clumps
    - t (int): The k-mers must appear at least t amount of times.
    Output:
    - list: A list of k-mers that occur at least t times in a window of length window_length in
    text.
    """
    if k <= 0 or window_length <= 0 or t <= 0:
        raise ValueError("Error: non-positive parameter given.")
    
    if len(text) == 0:
        raise ValueError("Error: empty string given.")
    
    if k > window_length:
        raise ValueError("Error: k bigger than window length.")
    
    if k > len(text):
        return []
    
    patterns: list[str] = []

    n = len(text)
    for i in range(0, n-window_length+1):
        current_window = text[i:i+window_length]
        freq_map = frequency_table(current_window, k)
        for s, val in freq_map.items():
            if val >= t and (s not in patterns):
                patterns.append(s)

    return patterns
