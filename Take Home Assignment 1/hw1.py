'''
Ashwika Sharma
Section AC
Implementing the functions for the Primer assessment.
'''


def total(n: int) -> int | None:
    """
    Returns the sum of the numbers from 0 to n (inclusive).
    If n is negative, returns None.
    """
    if n < 0:
        return None
    else:
        result = 0
        for i in range(n + 1):
            result += i
        return result


def is_relatively_prime(n: int, m: int) -> bool:
    """
    Takes in an integer n and integer m, and returns if the
    two numbers are relatively prime
    Relatively prime means not sharing any common factors other
    than 1.
    n and m are at least one, and the funciton returns a boolean
    true or false based on whether the numbers are relatively prime
    """
    if n < m:
        max = n
    else:
        max = m
    for i in range(2, max + 1):
        if n % i == 0 and m % i == 0:
            return False
    if n == 1 or m == 1:
        return True
    return True


def travel(directions: str, starting: tuple[int, int]) -> tuple[int, int]:
    """
    Takes in a string of directions and a tuple indicating the starting x and
    y position on a grid, where both are integers.
    Returns a tuple of two integers indicating the final position on the grid.
    'N' refers to increasing the y coordinate, 'S' is decreasing it
    'E' refers to increasing the x coordinate, 'W' is decreasing it
    Ignoring case, any other character is ignored.
    """
    x = starting[0]
    y = starting[1]
    for i in directions:
        if i == 'N' or i == 'n':
            y += 1
        elif i == 'S' or i == 's':
            y -= 1
        elif i == 'E' or i == 'e':
            x += 1
        elif i == 'W' or i == 'w':
            x -= 1
    return (x, y)


def get_average_in_range(list1: list[float], low: float, high: float) -> float:
    """
    Takes in a list of floats, and a float low and high.
    Returns a float value of the average of all the numbers in the list
    in range low(inclusive) to high(exclusive). If there are no values in the
    range, it returns 0.
    """
    total = 0
    count = 0
    for i in list1:
        if i >= low and i < high:
            total += i
            count += 1
    if count == 0:
        return 0
    else:
        return total/count


def longest_word(file_name: str) -> str | None:
    """
    Takes in a string filename and returns the longest word in the
    file as well as which line it is on as a string.
    A word is a sequence of characters seperated by whitespace
    If there are ties for longest word, it returns the first one in the file
    If there are no words in file/empty file it returns None.
    """
    longest = 0
    line = 0
    final_line = 0
    word = ''
    with open(file_name) as f:
        lines = f.readlines()
        for a in lines:
            line += 1
            words = a.split()
            for b in words:
                if len(b) > longest:
                    final_line = line
                    longest = len(b)
                    word = b
    if word == '':
        return None
    return (str(final_line) + ": " + word)


def mode_digit(n: int) -> int:
    """
    Takes in an integer n and returns digit that is most frequent
    in the number
    Regardless of the number sign, the digit returns is positive
    If there is a tie for most frequent, return the digit with
    the greatest value.
    """
    n = abs(n)
    tracking = {}
    while n > 0:
        keys = tracking.keys()
        digit = n % 10
        if digit not in keys:
            tracking[digit] = 0
        tracking[digit] += 1
        n = (n - n % 10)/10
    keys = tracking.keys()
    highest = 0
    digit = -1
    for key in keys:
        if tracking[key] > highest:
            digit = key
            highest = tracking[key]
        elif tracking[key] == highest:
            if digit < key:
                digit = key
    if digit == -1:
        return 0
    return digit


def reformat_date(date: str, current: str, target: str) -> str:
    """
    Takes in three strings representing the date, the current date
    format, and the target date format.
    Returns a string with the date formatted with the target format
    """
    today = date.split('/')
    current_format = current.split('/')
    target_format = target.split('/')
    result = ''
    end = 0
    for i in target_format:
        index = current_format.index(i)
        end += 1
        result += today[index]
        if end != len(target_format):
            result += "/"
    return result
