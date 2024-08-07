import pytest
from solution import find_minmax_indexes, find_negative_sum

def test_find_minmax_indexes_empty():
    with pytest.raises(ValueError, match='Input array is empty'):
        find_minmax_indexes([])

def test_find_minmax_indexes_single_element():
    assert find_minmax_indexes([5]) == (0, 0)

def test_find_minmax_indexes_all_positive():
    assert find_minmax_indexes([1, 2, 3, 4, 5]) == (0, 4)

def test_find_minmax_indexes_all_negative():
    assert find_minmax_indexes([-1, -2, -3, -4, -5]) == (4, 0)

def test_find_minmax_indexes_mixed_values():
    assert find_minmax_indexes([-1, 3, 0, 2, -5, 4]) == (4, 5)

def test_find_minmax_indexes_same_values():
    assert find_minmax_indexes([-2, -5, 1, -5, -3, -1, 4]) == (1, 6)

def test_find_negative_sum_empty():
    assert find_negative_sum([]) == 0

def test_find_negative_sum_single_positive_element():
    assert find_negative_sum([3]) == 0

def test_find_negative_sum_single_negative_element():
    assert find_negative_sum([-3]) == -3

def test_find_negative_sum_all_positive():
    assert find_negative_sum([1, 2, 3, 4, 5]) == 0

def test_find_negative_sum_all_negative():
    assert find_negative_sum([-1, -2, -3, -4, -5]) == -15

def test_find_negative_sum_mixed_values_inclusive():
    assert find_negative_sum([1, -2, 3, -4, 5], inclusive=True) == -4

def test_find_negative_sum_mixed_values_exclusive():
    assert find_negative_sum([1, -2, 3, -4, 5], inclusive=False) == 0

def test_find_negative_sum_inclusive():
    assert find_negative_sum([-3, -2, 1, 4, -1], inclusive=True) == -5

def test_find_negative_sum_exclusive():
    assert find_negative_sum([1, -2, -3, 4, -1], inclusive=False) == 0

def test_find_negative_sum_max_first():
    assert find_negative_sum([10, -2, -3, 1, 2, -5, 9, -4], inclusive=False) == -5

def test_find_negative_sum_min_first():
    assert find_negative_sum([1, -2, -5, 1, -3, -4, 9, 10], inclusive=False) == -7

def test_find_negative_sum_same_values():
    assert find_negative_sum([-2, -5, 1, -5, -3, -1, 4], inclusive=False) == -9

if __name__ == "__main__":
    pytest.main()
