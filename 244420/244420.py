def state_histogram(board: list[list[int]]) -> list[int]:
    """
    Compute a histogram of state frequencies in a board.

    Input:
        board (list[list[int]]): A rectangular board of integer states.

    Output:
        list[int]: A histogram list where hist[s] is the count of cells in state s,
                   for s = 0..max_state(board).
    """

    max_state = max(max(board))
    hist = [0] * (max_state+1)
    num_rows = len(board)
    num_cols = len(board[0])

    for r in range(num_rows):
        for c in range(num_cols):
            s = board[r][c]
            hist[s] += 1


    return hist 
