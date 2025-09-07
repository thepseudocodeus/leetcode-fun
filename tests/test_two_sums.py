import pytest
from two_sums.two_sums import TwoSum


def test_two_sum():
    assert TwoSum([2, 7, 11, 15], 9) == [0, 1]


def test_two_sum_2():
    assert TwoSum([3, 2, 4], 6) == [1, 2]


def test_two_sum_3():
    assert TwoSum([3, 3], 6) == [0, 1]
