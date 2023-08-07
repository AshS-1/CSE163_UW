'''
Ashwika Sharma
Section AC
This file deals with calculating certain descriptive statistics based on a
Pokemon dataset manually, using only built-in data structures and Math
functions. It includes methods such as ones to calculate the number of
unique types of Pokemon, the average attack value for Pokemon, and others.
'''
from cse163_utils import Pokemon


def species_count(dataset: list[Pokemon]) -> int:
    '''
    Takes in a list of Pokemon dataset and returns an integer that
    represents the number of unique pokemon species in the dataset.
    '''
    uniqueNames = set()
    for dict1 in dataset:
        if dict1['name'] not in uniqueNames:
            uniqueNames.add(dict1['name'])
    return len(uniqueNames)


def max_level(dataset: list[Pokemon]) -> tuple[str, int]:
    '''
    Takes in a list of Pokemon dataset. It identifies the pokemon with
    the highest level and returns a tuple with it's string name and
    integer level. If multiple pokemon have the same highest level,
    the pokemon that appears first in the file is returned in the tuple.
    '''
    highest = -1
    name = ''
    for dict1 in dataset:
        if dict1['level'] > highest:
            highest = dict1['level']
            name = dict1['name']
    return name, highest


def filter_range(dataset: list[Pokemon], lower: int, upper: int) -> list[str]:
    '''
    Takes in a list of Pokemon dataset, an integer for the lower bound,
    and a integer for the upper bound. Returns a list of strings of
    the names of the Pokemon whose levels fall between the lower
    and upper bound provided.
    '''
    result = []
    for dict1 in dataset:
        if dict1['level'] >= lower:
            if dict1['level'] < upper:
                result.append(dict1['name'])
    return result


def mean_attack_for_type(dataset: list[Pokemon], type1: str) -> float | None:
    '''
    Takes in a list of Pokemon dataset and a string type1. Returns a float of
    the average attack (atk) for all the pokemon in the dataset with the
    type provided. Returns None if there are no pokemon of the specified type.
    '''
    total = 0
    count = 0
    for dict1 in dataset:
        if dict1['type'] == type1:
            total += dict1['atk']
            count += 1
    if count == 0:
        return None
    else:
        return total/count


def count_types(dataset: list[Pokemon]) -> dict[str, int]:
    '''
    Takes in a list of Pokemon dataset and returns a dictionary of a
    string and integer. The dictionary represents each pokemon type
    and how many pokemon are there for each type.
    '''
    result = {}
    for dict1 in dataset:
        if dict1['type'] not in result:
            result[dict1['type']] = 0
        result[dict1['type']] = result[dict1['type']] + 1
    return result


def mean_attack_per_type(dataset: list[Pokemon]) -> dict[str, float]:
    '''
    Takes in a list of Pokemon dataset and returns and a dictionary of a
    string and float. The dictionary represents the average attack
    value for each pokemon type key.
    '''
    result = {}
    for dict1 in dataset:
        if dict1['type'] not in result:
            result[dict1['type']] = 0
        result[dict1['type']] = result[dict1['type']] + dict1['atk']
    final = {}
    x = result.keys()
    for key in x:
        final[key] = (result[key] / count_types(dataset)[key])
    return final
