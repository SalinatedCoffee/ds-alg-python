import pytest
from src.list.doublylinked_list import doublylinked_list

@pytest.fixture(name='empty_dll')
def fixture_empty_dll():
    """pytest fixture that instanciates a default doubly linked list."""
    return doublylinked_list()

def test_initialization(empty_dll):
    """Test object initialization."""
    assert len(empty_dll) == 0
    assert empty_dll._header._value is None
    assert empty_dll._trailer._value is None
    assert empty_dll._header._next == empty_dll._trailer
    assert empty_dll._trailer._prev == empty_dll._header

def test_insert_remove(empty_dll):
    """Test insert / remove methods."""
    first = empty_dll._insert_between(1, empty_dll._header, empty_dll._trailer)
    second = empty_dll._insert_between(3, first, empty_dll._trailer)
    third = empty_dll._insert_between(5, second, empty_dll._trailer)
    assert len(empty_dll) == 3
    assert empty_dll._delete_node(second) == 3
    assert len(empty_dll) == 2
    assert empty_dll._delete_node(third) == 5
    empty_dll._delete_node(first)
    assert len(empty_dll) == 0
    assert empty_dll._header._next == empty_dll._trailer
    assert empty_dll._trailer._prev == empty_dll._header
