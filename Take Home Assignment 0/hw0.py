'''
Ashwika Sharma
Section AC

Implementing the functions for the Startup assessment.
'''


def funky_sum(a: float, b: float, mix: float) -> float:
    '''
    Performs the weighted average of two floats a and b.
    Takes in the numbers a and b as well as the float mix that
    determines the relative amount to be using from a and from be
    If mix is less than or equal to 0, the function will return the value of a
    If mix is greater than or equal to 1, the funciton will return b
    If mix is between 0 and 1, the result would be the sum of a times the
    value of 1-mix and b times the value of mix. A float is always returned.
    '''
    if mix <= 0:
        return a
    elif mix >= 1:
        return b
    else:
        return (1 - mix) * a + mix * b


def total(n: int) -> int | None:
    '''
    Takes an integer n, and returns an integer, the sum of the
    integers between 0 and n inclusive.
    If n is negative, the function returns the value None.
    '''
    if n < 0:
        return None
    else:
        result = 0
        for i in range(n + 1):
            result += i
        return result


def swip_swap(source: str, c1: str, c2: str) -> str:
    '''
    Function takes in a string source and two strings c1 and c2
    Returns a string of the result in which the strings c1 and c2 are
    swapped, so c1 is in place of c2 and c2 is in place of c1
    '''
    result = ''
    for i in range(len(source)):
        if source[i] == c1:
            result += c2
        elif source[i] == c2:
            result += c1
        else:
            result += source[i]
    return result
