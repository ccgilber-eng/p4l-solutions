def diagonal_sum(matrix: list[list[int]]) -> int:
    """
    Compute the sum of the main diagonal entries in a square matrix.

    Parameters:
        matrix (list[list[int]]): A square integer matrix.

    Returns:
        int: The sum of the numbers on the main diagonal (top-left to bottom-right).
    """

    num_rows = len(matrix)
    num_cols = len(matrix[0])
    sum = 0
    for i in range(num_rows):
        sum += matrix[i][i]

    return sum 
    
