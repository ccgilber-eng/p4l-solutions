import random # this should be helpful!

# Write your simulate_one_birthday_trial() function here along with any subroutines that you need

def has_repeat(a: list[int]) -> bool:
    """
    Check if a list has repeat elements.

    Parameters:
    - a: a list of integers

    Returns:
    bool: True if a has repeat elements, False otherwise
    """
    
    read_values = []
    for val in a:
        if val in read_values:
            return True
            break 
        else: 
            read_values.append(val) 
    return False

def simulate_one_birthday_trial(num_people: int) -> bool:
    """
    Simulate one trial of the birthday game with num_people people.

    Parameters:
    - num_people (int): the number of people in the group

    Returns:
    bool: True if there is a collision, False otherwise
    """

    birthday_list = random.choices(range(1, 366), k=num_people)

    

    return has_repeat(birthday_list)

