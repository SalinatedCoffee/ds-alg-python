import pytest
from src.algo.sort import insertion_sort
from src.list.positional_list import positional_list

def convert_list(items):
    """Convert Python lists to PositionalDLLists."""
    subject = positional_list()
    for i in items:
        subject.add_last(i)
    return subject

def test_insertion_sort():
    """Test insertion sort on various scenarios."""
    basic_unsorted = [5, 2, 4, 3, 1]
    basic_unsorted_target = [1, 2, 3, 4, 5]
    basic_unsorted = convert_list(basic_unsorted)
    insertion_sort(basic_unsorted)
    for i, n in enumerate(basic_unsorted):
        assert basic_unsorted_target[i] == n
    all_identical = [1, 1, 1, 1, 1]
    all_identical_item = 1
    all_identical = convert_list(all_identical)
    insertion_sort(all_identical)
    for n in all_identical:
        assert n == all_identical_item
