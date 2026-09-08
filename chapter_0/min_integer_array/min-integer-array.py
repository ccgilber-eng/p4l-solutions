def min_integer_array(lst: list[int]) -> int:
    """
    Return the minimum integer in a non-empty list.
    Args:
        lst: A non-empty list of integers.
    Returns:
        The smallest integer in lst.
    Raises:
        ValueError: If lst is empty.
    """
    if len(lst)==0:
        raise ValueError("Error: empty list given to function.")

    m=lst[0]

    for val in lst:
        if val<m:
            m=val

    return m
