from pyparsing import empty
import pytest
from src.map.unsorted_map import unsorted_map

@pytest.fixture(name='empty_map')
def fixture_empty_map():
    """pytest fixture that returns an empty unsorted_map."""
    return unsorted_map()

@pytest.fixture(name='sample_map')
def fixture_sample_map():
    """pytest fixture that returns an unsorted_map that already contains items."""
    items = [('A', 11), ('B', 3), ('C', 7), ('G', 5)]
    ret = unsorted_map()
    for i in items:
        ret[i[0]] = i[1]
    if len(items) != len(ret):
        raise Exception('Failed to construct correct table map')
    return ret

def test_initialization(empty_map):
    """Tests object instantiation."""
    assert len(empty_map) == 0
    with pytest.raises(KeyError):
        empty_map['A']

def test_add_items(empty_map):
    """Tests the addition of items to an empty map."""
    empty_map['A'] = 1
    assert len(empty_map) == 1
    empty_map['B'] = 3
    empty_map['C'] = 5
    assert len(empty_map) == 3

def test_item_retrieval(sample_map):
    """Tests the retrieval of values given a key."""
    assert sample_map['A'] == 11
    assert sample_map.get('A') == 11
    with pytest.raises(KeyError):
        sample_map['Z']
    assert sample_map['B'] == 3
    assert sample_map['C'] == 7
    assert sample_map['G'] == 5

def test_remove_items(sample_map):
    """Tests the removal of items."""
    init_size = len(sample_map)
    del sample_map['A']
    assert len(sample_map) == init_size - 1
    with pytest.raises(KeyError):
        sample_map['A']
    with pytest.raises(KeyError):
        del sample_map['Z']
    assert sample_map.pop('B') == 3
    del sample_map['C']
    del sample_map['G']
    assert len(sample_map) == init_size - 4

def test_mutation_items(sample_map):
    """Tests the mutation of items."""
    sample_map['A'] = 123
    assert sample_map['A'] == 123

def test_iterator(sample_map):
    """Tests the behavior of the overriden iterator method."""
    count = 0
    items = ['A', 'B', 'C', 'G']
    for idx, key in enumerate(sample_map):
        assert key == items[idx]
        count += 1
    assert count == len(items)
