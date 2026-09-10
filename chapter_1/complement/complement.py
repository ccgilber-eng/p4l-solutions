# Insert your complement() function here.
def complement(dna: str) -> str:
    """
    Finds the complementary strand of the given string.

    Parameters:
    - dna (str): A dna string.

    Returns:
    - str: the string whose i-th symbol is the complementary 
    nucleotide of the i-th symbol of the input string. (A-T, C-G, T-A, G-C).
    """
    dna2 = ""

    for i, symbol in enumerate(dna):
        match symbol:
            case "A": 
                dna2 += "T"
            case "C":
                dna2 += "G"
            case "G":
                dna2 += "C"
            case "T":
                dna2 += "A"
            case _:
                raise ValueError("Not allowed.")

          
    return dna2 
