'''
Ashwika Sharma
Section AC
Tests the functions in hw2_manual and hw2_pandas with a
provided dataset and one that I've created.
'''

import pandas as pd


from cse163_utils import assert_equals, Pokemon

import hw2_manual
import hw2_pandas
import cse163_utils

# If you want to include more global constants,
# please check the code quality guide!
SPEC_TEST_FILE = "/home/pokemon_test.csv"
OWN_TEST_FILE = "/home/pokemon_own_test.csv"


def test_max_level(test_data: list[Pokemon], test_df: pd.DataFrame,
                   own_data: list[Pokemon], own_df: pd.DataFrame) -> None:
    '''
    Tests max_level by taking in a list of Pokemon test_data and own_data,
    and DataFrames test_df and own_df. Test and own correspond to different
    csv files. Returns None.
    '''
    assert_equals(('Lapras', 72), hw2_manual.max_level(test_data))
    assert_equals(('Lapras', 72), hw2_pandas.max_level(test_df))
    assert_equals((' Bulbasaur', 99), hw2_manual.max_level(own_data))
    assert_equals((' Bulbasaur', 99), hw2_pandas.max_level(own_df))


def test_filter_range(test_data: list[Pokemon], test_df: pd.DataFrame,
                      own_data: list[Pokemon], own_df: pd.DataFrame) -> None:
    '''
    Tests filter_range by taking in a list of Pokemon test_data and own_data,
    and DataFrames test_df and own_df. Test and own correspond to different
    csv files. Returns None.
    '''
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'],
                  hw2_manual.filter_range(test_data, 35, 72))
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'],
                  hw2_pandas.filter_range(test_df, 35, 72))
    assert_equals([' Bulbasaur', ' Laprase'],
                  hw2_manual.filter_range(own_data, 12, 67))
    assert_equals([' Bulbasaur', ' Laprase'],
                  hw2_pandas.filter_range(own_df, 12, 67))


def test_mean_attack_for_type(test_data: list[Pokemon], test_df: pd.DataFrame,
                              own_data: list[Pokemon],
                              own_df: pd.DataFrame) -> None:
    '''
    Tests mean_attack_for_type by taking in a list of Pokemon test_data
    and own_data, and DataFrames test_df and own_df. Test and own
    correspond to different csv files. Returns None.
    '''
    assert_equals(47.5, hw2_manual.mean_attack_for_type(test_data, 'fire'))
    assert_equals(47.5, hw2_pandas.mean_attack_for_type(test_df, 'fire'))
    assert_equals(None, hw2_manual.mean_attack_for_type(own_data, 'fire'))
    assert_equals(None, hw2_pandas.mean_attack_for_type(own_df, 'fire'))


def test_count_types(test_data: list[Pokemon], test_df: pd.DataFrame,
                     own_data: list[Pokemon], own_df: pd.DataFrame) -> None:
    '''
    Tests count_types by taking in a list of Pokemon test_data and own_data,
    and DataFrames test_df and own_df. Test and own correspond to different
    csv files. Returns None.
    '''
    assert_equals({'fire': 2, 'water': 2}, hw2_manual.count_types(test_data))
    assert_equals({'fire': 2, 'water': 2}, hw2_pandas.count_types(test_df))
    assert_equals({' fire': 3, ' water': 1, ' electric': 2},
                  hw2_manual.count_types(own_data))
    assert_equals({' fire': 3, ' water': 1, ' electric': 2},
                  hw2_pandas.count_types(own_df))


def test_species_count(test_data: list[Pokemon], test_df: pd.DataFrame,
                       own_data: list[Pokemon], own_df: pd.DataFrame) -> None:
    '''
    Tests species_count by taking in a list of Pokemon test_data and own_data,
    and DataFrames test_df and own_df. Test and own correspond to different
    csv files. Returns None.
    '''
    assert_equals(3, hw2_manual.species_count(test_data))
    assert_equals(3, hw2_pandas.species_count(test_df))
    assert_equals(3, hw2_manual.species_count(own_data))
    assert_equals(3, hw2_pandas.species_count(own_df))


def test_mean_attack_per_type(test_data: list[Pokemon], test_df: pd.DataFrame,
                              own_data: list[Pokemon],
                              own_df: pd.DataFrame) -> None:
    '''
    Tests mean_attack_per_type by taking in a list of Pokemon test_data and
    own_data, and DataFrames test_df and own_df. Test and own correspond to
    different csv files. Returns None.
    '''
    assert_equals({'fire': 47.5, 'water': 140.5},
                  hw2_manual.mean_attack_per_type(test_data))
    assert_equals({'fire': 47.5, 'water': 140.5},
                  hw2_pandas.mean_attack_per_type(test_df))
    assert_equals({' water': 20.0, ' fire': 61.0, ' electric': 28.0},
                  hw2_manual.mean_attack_per_type(own_data))
    assert_equals({' water': 20.0, ' fire': 61.0, ' electric': 28.0},
                  hw2_pandas.mean_attack_per_type(own_df))


def main():
    test_df = pd.read_csv(SPEC_TEST_FILE)
    test_data = cse163_utils.parse(SPEC_TEST_FILE)
    own_df = pd.read_csv(OWN_TEST_FILE)
    own_data = cse163_utils.parse(OWN_TEST_FILE)
    test_max_level(test_data, test_df, own_data, own_df)
    test_filter_range(test_data, test_df, own_data, own_df)
    test_mean_attack_for_type(test_data, test_df, own_data, own_df)
    test_count_types(test_data, test_df, own_data, own_df)
    test_species_count(test_data, test_df, own_data, own_df)
    test_mean_attack_per_type(test_data, test_df, own_data, own_df)


if __name__ == '__main__':
    main()
