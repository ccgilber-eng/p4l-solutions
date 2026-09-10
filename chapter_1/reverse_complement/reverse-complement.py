# Write your reverse_complement() function here, along with any subroutines that you need.
def reverse_complement(dna: str) -> str:
    """
    Compute the reverse complement of a DNA string.

    Args:
        dna: A DNA string.
    Returns:
        The reverse complement of the DNA string.
    """

    def complement(dna):
    
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

    def reverse(s: str) -> str:
        characters = [] 
        n = len(s) 
        for i in range(n):
            characters.append(s[n-1-i])
    
        return "".join(characters)


    return reverse(complement(dna))

    
