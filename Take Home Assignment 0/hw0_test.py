'''
Ashwika Sharma
Section AC
Testing the functions for the Startup assessment.
'''

import hw0

from cse163_utils import assert_equals


def test_funky_sum() -> bool:
    '''
    Testing the function funky_sum
    '''
    assert_equals(2.0, hw0.funky_sum(1, 3, 0.5))
    assert_equals(1, hw0.funky_sum(1, 3, 0))
    assert_equals(1.5, hw0.funky_sum(1, 3, 0.25))
    assert_equals(2.2, hw0.funky_sum(1, 3, 0.6))
    assert_equals(3, hw0.funky_sum(1, 3, 1))
    assert_equals(1, hw0.funky_sum(1, 3, -1))
    assert_equals(3, hw0.funky_sum(1, 3, 2))


def test_total() -> bool:
    '''
    Testing the function total
    '''
    # The regular case
    assert_equals(15, hw0.total(5))
    # Seems likely we could mess up 0 or 1
    assert_equals(1, hw0.total(1))
    assert_equals(0, hw0.total(0))
    # TODO: add your own total test here
    assert_equals(None, hw0.total(-1))


def test_swip_swap() -> bool:
    '''
    Testing the function swip_swap
    '''
    assert_equals('offbar', hw0.swip_swap('foobar', 'f', 'o'))
    assert_equals('foocar', hw0.swip_swap('foobar', 'b', 'c'))
    assert_equals('foobar', hw0.swip_swap('foobar', 'z', 'c'))
    assert_equals('bnanan', hw0.swip_swap('banana', 'a', 'n'))
    assert_equals('ginsgons', hw0.swip_swap('singsong', 's', 'g'))


def main():
    test_funky_sum()
    test_total()
    test_swip_swap()


if __name__ == '__main__':
    main()
