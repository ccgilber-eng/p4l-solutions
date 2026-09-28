import random  # this should be helpful!


def probability_of_repeated_kmer(num_trials: int, n: int, k: int, alphabet_size: int) -> float:
    """
    Estimate the probability that a random genome contains two equal k-mers.

    Parameters:
        num_trials (int)    - How many random genomes to build (at least 1).
        n (int)             - The length of each random genome.
        k (int)             - The length of the k-mers to compare.
        alphabet_size (int) - How many distinct symbols the genome is built from.

    Returns:
        float - The fraction of the random genomes that contained some k-mer twice.
    """

    if n < k + 1:
        return 0.0

    count = 0
    for i in range(num_trials):
        genome = random.choices(range(alphabet_size), k=n)
        kmers = set()
        for d in range(n-k+1):
            substring = tuple(genome[d: d+k])
            if substring in kmers:
                count += 1
                break 
            kmers.add(substring)
                

    return count / num_trials


   
