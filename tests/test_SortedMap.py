import pytest
from src.map.sorted_map import sorted_map

@pytest.fixture(name='empty_map')
def fixture_empty_map():
    return sorted_map()

def test_initialization(empty_map):
    """Tests object instantiation."""
    assert len(empty_map) == 0

def test_add_items():
    """Tests the addition of key-value pairs."""
    assert False

def test_access_items():
    """Tests the modification of a value given its key."""
    assert False

def test_remove_items():
    """Tests the removal of key-value pairs."""
    assert False

def test_ge_gt():
    """Tests the behavior of 'greater-than' search methods."""
    assert False

def test_le_lt():
    """Tests the behavior of 'less-than' search methods."""
    assert False

def test_iter():
    """Tests the behavior of custom iterator methods."""
    assert False

def test_iter_range():
    """Tests the behavior of sorted_map.find_range()."""
    assert False
