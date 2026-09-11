# Insert your prefixes() function here.
def prefixes(s: str) -> list[str]:
    """
    Return a list of all prefixes of the string s.

    Parameters:
        s (str) - The input string.

    Returns:
        list[str] - A list of prefixes of s, starting with the empty string ""
                    and ending with s itself.
    """
    prefix_list = []
    k = len(s)
    for i in range(0, k+1):
        substring = s[0:i]
        prefix_list.append(substring)
    return prefix_list

        
