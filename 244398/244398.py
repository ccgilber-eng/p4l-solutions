def min_window_skew(genome: str, window_len: int) -> list[int]:
    """
    Return all start indices of windows of length window_len in genome
    that achieve the minimum GC-skew.

    Parameters:
        genome (str): A nonempty DNA string consisting of 'A', 'C', 'G', 'T'.
        window_len (int): The length of the window (1 ≤ window_len ≤ len(genome)).

    Returns:
        (list[int]): A list of start indices (0-based) in increasing order 
                   where the window skew is minimal.
                   If window_len > len(genome), return [].
    """
    if window_len > len(genome):
        return []
    if genome == "":
        raise ValueError("String cannot be empty.")
    
    skews = []
    window_count = len(genome) - window_len + 1
    
    for i in range(window_count):
        window_substring = genome[i:i + window_len]
        g_count = 0
        c_count = 0
        for character in window_substring:
            if character == "G":
                g_count += 1
            if character == "C":
                c_count += 1
        skew = g_count - c_count 
        skews.append(skew)

    min_skew = min(skews) 
    min_i = []
    for i in range(window_count):
        if skews[i] == min_skew:
            min_i.append(i)
    
    return min_i

        


    
