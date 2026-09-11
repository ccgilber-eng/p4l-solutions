def rc_match_at(pattern: str, text: str, i: int) -> bool:
    """
    Return True if either the given DNA pattern or its reverse complement 
    occurs in the text starting at position i, otherwise return False.

    Parameters:
        pattern (str): A DNA string consisting of 'A', 'C', 'G', 'T'.
        text (str): The DNA text to search within.
        i (int): The starting index in text to check for the match.

    Returns:
        bool: True if pattern or its reverse complement matches text[i:],
              False otherwise.
    """

    complement = ""
    

    compl_dict: dict[str, str] = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }

    for letter in pattern:
        complement += compl_dict[letter]


    characters = [] 
    n = len(pattern) 
    for j in range(n):
        characters.append(complement[n-1-j])
    
    reverse_complement = "".join(characters) 

    
    if pattern == text[i: i + len(pattern)] or text[i: i + len(pattern)] == reverse_complement:
        return True 

    else:
        return False 
