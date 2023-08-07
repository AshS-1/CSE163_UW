'''
Ashwika Sharma
Section AC
Testing the functions for the Primer assessment.
'''
import hw1

from cse163_utils import assert_equals


def test_total() -> None:
    """
    Tests the total method
    """
    # The regular case
    assert_equals(15, hw1.total(5))
    # Seems likely we could mess up 0 or 1
    assert_equals(1, hw1.total(1))
    assert_equals(0, hw1.total(0))

    # Test the None case
    assert_equals(None, hw1.total(-1))


def test_is_relatively_prime() -> None:
    """
    Tests the is_relatively_prime method
    """
    assert_equals(False, hw1.is_relatively_prime(12, 14))
    assert_equals(True, hw1.is_relatively_prime(5, 9))
    assert_equals(True, hw1.is_relatively_prime(8, 9))
    assert_equals(True, hw1.is_relatively_prime(8, 1))
    assert_equals(False, hw1.is_relatively_prime(14, 28))
    assert_equals(True, hw1.is_relatively_prime(1, 4))


def test_travel() -> None:
    """
    Tests the travel method
    """
    assert_equals((-1, 4), hw1.travel('NW!ewnW', (1, 2)))
    assert_equals((0, 5), hw1.travel('SEW13NN', (0, 4)))
    assert_equals((-9, 7), hw1.travel('363218', (-9, 7)))


def test_reformat_date() -> None:
    """
    Tests the reformat_date method
    """
    assert_equals('3/1/2', hw1.reformat_date('1/2/3', 'M/D/Y', 'Y/M/D'))
    assert_equals('4/0', hw1.reformat_date('0/200/4', 'Y/D/M', 'M/Y'))
    assert_equals('2', hw1.reformat_date('3/2', 'M/D', 'D'))
    assert_equals('31/12/1998', hw1.reformat_date('12/31/1998', 'M/D/Y',
                                                                'D/M/Y'))
    assert_equals('12/32', hw1.reformat_date('12/5/32', 'D/M/Y', 'D/Y'))
    assert_equals('8', hw1.reformat_date('5/8/10', 'D/Y/M', 'Y'))


def test_get_average_in_range() -> None:
    """
    Tests the get_average_in_range method
    """
    assert_equals(5.5, hw1.get_average_in_range([1, 5, 6, 7, 9], 5, 7))
    assert_equals(2.0666666, hw1.get_average_in_range([1, 2, 3.2], -1, 10))
    assert_equals(0, hw1.get_average_in_range([1, 2, 3, 10002], 10, 15))
    assert_equals(-1, hw1.get_average_in_range([-7, -5, 3, 10], -6, 6))


def test_longest_word() -> None:
    """
    Tests the longest_word method
    """
    assert_equals('3: Merrily,', hw1.longest_word('/home/song.txt'))
    assert_equals('3: ashwika', hw1.longest_word('/home/test1.txt'))
    assert_equals(None, hw1.longest_word('/home/test2.txt'))


def test_mode_digit() -> None:
    """
    Tests the mode_digit method
    """
    assert_equals(1, hw1.mode_digit(12121))
    assert_equals(0, hw1.mode_digit(0))
    assert_equals(2, hw1.mode_digit(-122))
    assert_equals(2, hw1.mode_digit(1211232231))
    assert_equals(9, hw1.mode_digit(-549283))
    assert_equals(7, hw1.mode_digit(5555577777))


def main():
    test_total()
    test_get_average_in_range()
    test_is_relatively_prime()
    test_longest_word()
    test_mode_digit()
    test_reformat_date()
    test_travel()


if __name__ == '__main__':
    main()
