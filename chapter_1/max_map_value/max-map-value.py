 

# Insert your max_map_value() function here.
def max_map_value(dict_values: dict) -> int:
    """
    max_map_value finds the maximum value of a given dictionary.

    Parameters:
    - dict_values (dict): A dictionary that has integers as values.

    Retursn:
    - int: The highest value key in the given dictionary.
    """
    if len(dict_values) == 0:
        raise ValueError("Error: empty map given.")
    vals = list(dict_values.values())
    m = vals[0]

    for val in vals:
        if val > m:
            m = val
    return m
