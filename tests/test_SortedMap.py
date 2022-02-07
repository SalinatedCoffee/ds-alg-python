import pytest
from src.map.sorted_map import sorted_map

@pytest.fixture(name='empty_map')
def fixture_empty_map():
    """pytest fixture that returns an empty sorted_map object."""
    return sorted_map()

@pytest.fixture(name='sample_map')
def fixture_sample_map():
    """pytest fixture that returns a populated sorted_map object."""
    # TODO: maybe use pytest globals for test data
    tuples = [(1, 'One'), (3, 'Three'), (4, 'Four'), (5, 'Five'), (7, 'Seven')]
    ret = sorted_map()
    for k, v in tuples:
        ret[k] = v
    if len(tuples) != len(ret):
        raise Exception('Failed to construct correct map object')
    return ret

def test_initialization(empty_map):
    """Tests object instantiation."""
    assert len(empty_map) == 0

def test_add_items(empty_map):
    """Tests the addition of key-value pairs."""
    empty_map[2] = 'Two'
    assert len(empty_map) == 1
    empty_map[1] = 'One'
    empty_map[5] = 'Five'
    assert len(empty_map) == 3

def test_access_items(sample_map):
    """Tests the modification of a value given its key."""
    assert sample_map[1] == 'One'
    with pytest.raises(KeyError):
        sample_map[2]
    sample_map[1] = 'Uno'
    assert sample_map[1] == 'Uno'

def test_remove_items(sample_map):
    """Tests the removal of key-value pairs."""
    init = len(sample_map)
    del sample_map[1]
    del sample_map[3]
    assert len(sample_map) == init - 2
    with pytest.raises(KeyError):
        sample_map[1]
    with pytest.raises(KeyError):
        del sample_map[2]

def test_get_min_max(sample_map, empty_map):
    """Tests the behavior of find min/max methods."""
    assert sample_map.find_min() == (1, 'One')
    assert sample_map.find_max() == (7, 'Seven')
    del sample_map[1]
    assert sample_map.find_min() == (3, 'Three')
    del sample_map[7]
    assert sample_map.find_max() == (5, 'Five')
    sample_map[2] = 'Two'
    assert sample_map.find_min() == (2, 'Two')
    sample_map[6] = 'Six'
    assert sample_map.find_max() == (6, 'Six')
    
    assert empty_map.find_min() is None
    assert empty_map.find_max() is None

def test_ge_gt(sample_map, empty_map):
    """Tests the behavior of 'greater-than' search methods."""
    assert sample_map.find_ge(1) == (1, 'One')
    assert sample_map.find_ge(2) == (3, 'Three')
    assert sample_map.find_gt(1) == (3, 'Three')
    assert sample_map.find_gt(2) == (3, 'Three')
    assert sample_map.find_ge(7) == (7, 'Seven')
    assert sample_map.find_ge(8) is None
    assert sample_map.find_gt(7) is None
    assert sample_map.find_gt(8) is None

    assert empty_map.find_ge(0) is None
    assert empty_map.find_gt(0) is None

def test_le_lt(sample_map, empty_map):
    """Tests the behavior of 'less-than' search methods."""
    assert sample_map.find_le(7) == (7, 'Seven')
    assert sample_map.find_le(6) == (5, 'Five')
    assert sample_map.find_lt(7) == (5, 'Five')
    assert sample_map.find_lt(6) == (5, 'Five')
    assert sample_map.find_le(1) == (1, 'One')
    assert sample_map.find_le(0) is None
    assert sample_map.find_lt(1) is None
    assert sample_map.find_lt(0) is None

    assert empty_map.find_le(0) is None
    assert empty_map.find_lt(0) is None

def test_iter(sample_map):
    """Tests the behavior of custom iterator methods."""
    keys = [1, 3, 4, 5, 7]
    for k, n in zip(keys, sample_map):
        assert k == n
    for k, n in zip(reversed(keys), reversed(sample_map)):
        assert k == n

def test_iter_range(sample_map):
    """Tests the behavior of sorted_map.find_range()."""
    keys = [1, 3, 4, 5, 7]
    for k, n in zip(keys, sample_map.find_range(None, None)):
        assert k == n[0]
    for k, n in zip(keys[:3], sample_map.find_range(None, 5)):
        assert k == n[0]
    for k, n in zip(keys[2:], sample_map.find_range(4, None)):
        assert k == n[0]
    for k, n in zip(keys[1:4], sample_map.find_range(3, 7)):
        assert k == n[0]
