import pytest
from src.list.positional_list import positional_list

@pytest.fixture(name='empty_positional')
def fixture_empty_positional():
    """pytest fixture that generates a default, empty positional list."""
    return positional_list()

def test_initialization(empty_positional):
    """Test object initialization."""
    assert len(empty_positional) == 0
    assert empty_positional.first() is None
    assert empty_positional.last() is None
    with pytest.raises(TypeError):
        empty_positional.before(None)
    p = positional_list.Position(None, None)
    with pytest.raises(ValueError):
        empty_positional.before(p)

def test_insert_remove(empty_positional):
    """Test insert / removal of items."""
    first = empty_positional.add_first(3)
    second = empty_positional.add_first(5)
    third = empty_positional.add_first(7)
    assert len(empty_positional) == 3
    assert empty_positional.first() == third
    assert empty_positional.last() == first
    assert empty_positional.delete(first) == 3
    with pytest.raises(ValueError):
        empty_positional.before(first)
    assert empty_positional.first().element() == 7
    empty_positional.delete(second)
    empty_positional.delete(third)
    assert len(empty_positional) == 0

def test_replace(empty_positional):
    """Test value replace method."""
    pos = empty_positional.add_first(101)
    assert pos.element() == 101
    assert empty_positional.replace(pos, 42) == 101
    assert pos.element() == 42

def test_iterator(empty_positional):
    """Test __iter__ override."""
    for i in range(7):
        empty_positional.add_last(i)

    assert len(empty_positional) == 7
    for pos, i in enumerate(empty_positional):
        assert pos == i