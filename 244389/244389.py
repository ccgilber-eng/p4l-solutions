import sys
import math 

# Please do not remove package declarations because these are used by the autograder.
# You may declare additional packages above if needed.


# Insert your isAmicable(a, b) function here, along with any subroutines that you need.
# The function should return a boolean: True if (a, b) are amicable, otherwise False.
def isAmicable(a: int, b: int) -> bool:
    if a<=1 or b <= 1:
        return False

    sum_a = 1
    for i in range(2, int(math.isqrt(a)) + 1):
        if a%i==0:
            sum_a += i
            if i!=(a//i):
                sum_a += (a//i)

    sum_b = 1
    for d in range(2, int(math.isqrt(b)) + 1):
        if b%d==0:
            sum_b += d
            if d!=(b//d):
                sum_b += (b//d)

    if sum_a==b and sum_b==a:
        return True
    else:
        return False 





