def boards_equal(board1: list[list[bool]], board2: list[list[bool]]) -> bool:
    """
    Check if two Game of Life boards are exactly the same.

    Parameters:
        board1 (list[list[bool]]): The first Game of Life board.
        board2 (list[list[bool]]): The second Game of Life board.

    Returns:
        bool: True if the boards have the same dimensions and identical values 
              in every position, False otherwise.
    """

    num_rows_1 = len(board1)
    num_rows_2 = len(board2)
    if num_rows_1 >= 1 and num_rows_2 >= 1:
        num_cols_1 = len(board1[0])
        num_cols_2 = len(board2[0])
    else:
        return True
        

    if num_rows_1 != num_rows_2 or num_cols_1 != num_cols_2: 
        return False
    
    if num_cols_1 == 0 or num_cols_2 == 0 or num_rows_1 == 0 or num_rows_2 == 0:
        return True
    
    for i in range(num_rows_1):
        if board1[i] != board2[i]:
            return False
            break
    return True 

