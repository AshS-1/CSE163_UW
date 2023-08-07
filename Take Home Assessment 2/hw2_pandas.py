'''
Ashwika Sharma
Section AC
This file deals with calculating certain descriptive statistics using the
Pandas library. It includes methods such as ones to calculate the number of
unique types of Pokemon, the average attack value for Pokemon, and others.
'''

import pandas as pd


def species_count(group: pd.DataFrame) -> int:
    '''
    Takes in a Pandas DataFrame and returns an integer that
    represents the number of unique pokemon species in the dataset.
    '''
    return len(group['name'].unique())


def filter_range(data: pd.DataFrame, lower: int, higher: int) -> list[str]:
    '''
    Takes in a Pandas DataFrame, an integer for the lower bound,
    and a integer for the upper bound. Returns a list of strings of
    the names of the Pokemon whose levels fall between the lower
    and upper bound provided.
    '''
    final = data[(data.level >= lower) & (data.level < higher)]
    result = []
    for i in final.index:
        result.append(final['name'][i])
    return result


def max_level(data: pd.DataFrame) -> tuple[str, int]:
    '''
    Takes in a Pandas DataFrame. It identifies the pokemon with
    the highest level and returns a tuple with it's string name and
    integer level. If multiple pokemon have the same highest level,
    the pokemon that appears first in the file is returned in the tuple.
    '''
    highest = 0
    name = ''
    for i in data.index:
        if data['level'][i] > highest:
            highest = data['level'][i]
            name = data['name'][i]
    result = (name, highest)
    return result


def count_types(data: pd.DataFrame) -> dict[str, int]:
    '''
    Takes in a Pandas DataFrame and returns a dictionary of a
    string and integer. The dictionary represents each pokemon type
    and how many pokemon are there for each type.
    '''
    return dict(data.groupby('type')['type'].count())


def mean_attack_per_type(data: pd.DataFrame) -> dict[str, float]:
    '''
    Takes in a Pandas DataFrame and returns and a dictionary of a
    string and float. The dictionary represents the average attack
    value for each pokemon type key.
    '''
    return dict(data.groupby('type')['atk'].mean())


def mean_attack_for_type(data: pd.DataFrame, type1: str) -> float | None:
    '''
    Takes in a Pandas DataFrame and a string type1. Returns a float of
    the average attack (atk) for all the pokemon in the dataset with the
    type provided. Returns None if there are no pokemon of the specified type.
    '''
    new = data[data['type'] == type1]
    if new.empty:
        return None
    return new['atk'].mean()
