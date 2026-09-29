import random # this should be helpful!

# Write your shared_birthday_probability() function here along with any subroutines that you need

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


def shared_birthday_probability(num_people: int, num_trials: int) -> float:
    """
    Compute the probability that two people in a group of num_people have the same birthday, after running
    num_trials trials.

    Parameters:
    - num_people (int): the number of people in the group
    - num_trials (int): the number of trials to run

    Returns:
    float: the average probability that two people in a group of num_people have the same birthday
    """

    count = 0
    for i in range(num_trials):
        if simulate_one_birthday_trial(num_people) == True:
            count += 1

    return count / num_trials 
