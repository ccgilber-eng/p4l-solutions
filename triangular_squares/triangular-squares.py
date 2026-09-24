import sys
import math 

# Please do not remove package declarations because these are used by the autograder. 
# If you need additional packages, then you may declare them above.


# Insert your triandsq(n) function here, along with any subroutines that you need.
# The function should return a list of triangular and square numbers under n.

def is_perfect_square(i):
    root = math.isqrt(i)
    if root**2 == i:
        return True
    return False


def is_triangular(i):
    current_value = 0
    a = 1
    while current_value < i:
        current_value += a
        a += 1

    if current_value == i:
        return True
    return False 


def triandsq(n):
    triangular_squares = []
    for i in range(1, n):
        if is_perfect_square(i) == True:
            if is_triangular(i) == True:
                triangular_squares.append(i)
        
    return triangular_squares





