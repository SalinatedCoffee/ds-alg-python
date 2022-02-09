import pytest
from src.map.tree_map import tree_map

@pytest.fixture(name='empty_map')
def fixture_empty_map():
    """pytest fixture that returns an empty tree_map."""
    return tree_map()

@pytest.fixture(name='sample_map')
def fixture_sample_map():
    """pytest fixture that returns a populated tree_map."""
    ret = tree_map()
    # tree_map does not self balance, so insert pairs accordingly
    tuples = [(3, 'Three'), (1, 'One'), (5, 'Five'), (4, 'Four'), (7, 'Seven')]
    for k, v in tuples:
        ret[k] = v
    if len(tuples) != len(ret):
        raise Exception('Failed to construct correct tree_map')
    return ret

def test_initialization(empty_map):
    """Tests object instantiation."""
    assert len(empty_map) == 0

def test_add_items_map(empty_map):
    """Tests the addition of items via MutableMapping methods."""
    empty_map[1] = 'One'
    assert len(empty_map) == 1
    empty_map[2] = 'Two'
    empty_map[3] = 'Three'
    assert len(empty_map) == 3

def test_access_items(sample_map):
    """Tests the access of items via public methods."""
    # methods defined in tree_map
    assert isinstance(sample_map.find_position(1), tree_map.Position)
    assert sample_map.find_position(2) is None
    assert sample_map.find_position(1).value == 'One'
    assert sample_map.find_position(3).value == 'Three'
    assert sample_map.find_position(7).value == 'Seven'

    # methods inherited from linkedbinary_tree
    root = sample_map.root()
    assert root is not None
    assert root.key() == 3
    assert sample_map.left(root).key() == 1
    assert sample_map.right(root).key() == 5


def test_access_items_map(sample_map):
    """Tests the access of items via MutableMapping methods."""
    with pytest.raises(KeyError):
        sample_map[2]
    assert sample_map[1] == 'One'
    assert sample_map[3] == 'Three'
    assert sample_map[5] == 'Five'

def test_remove_items(sample_map):
    """Tests the removal of items via public methods."""
    init = len(sample_map)
    seven = sample_map.find_position(7)
    sample_map.delete(seven)
    assert len(sample_map) == init - 1
    three = sample_map.find_position(3)
    sample_map.delete(three)
    five = sample_map.find_position(5)
    sample_map.delete(five)
    assert len(sample_map) == init - 3
    assert sample_map.root().key() == 1

def test_remove_items_map(sample_map):
    """Tests the removal of items via MutableMapping methods."""
    init = len(sample_map)
    del sample_map[7]
    assert len(sample_map) == init - 1
    del sample_map[3]
    del sample_map[5]
    assert len(sample_map) == init - 3
    assert sample_map.root().key() == 1

def test_relative_search(sample_map, empty_map):
    """Tests the relative find methods."""
    # operations on freshly generated tree
    assert sample_map.first().key() == 1
    assert sample_map.last().key() == 7
    assert sample_map.find_min() == (1, 'One')
    assert sample_map.find_max() == (7, 'Seven')
    five = sample_map.find_position(5)
    assert sample_map.before(five).key() == 4
    assert sample_map.after(five).key() == 7
    assert sample_map.find_ge(6) == (7, 'Seven')
    assert sample_map.find_ge(7) ==  (7, 'Seven')
    assert sample_map.find_le(2) == (1, 'One')
    assert sample_map.find_le(1) == (1, 'One')

    # operations on tree with some items removed
    del sample_map[1]
    del sample_map[7]
    assert sample_map.first().key() == 3
    assert sample_map.last().key() == 5
    assert sample_map.find_min() == (3, 'Three')
    assert sample_map.find_max() == (5, 'Five')

    # operations that should return None
    assert empty_map.first() is None
    assert empty_map.last() is None
    assert empty_map.find_min() is None
    assert empty_map.find_max() is None
    assert empty_map.find_ge(1) is None
    assert empty_map.find_le(1) is None
    assert sample_map.find_ge(10) is None
    assert sample_map.find_le(1) is None
    assert sample_map.root().left() is None

def test_iterators(sample_map):
    """Tests the generator methods."""
    keys = [1, 3, 4, 5, 7]
    for k, i in zip(keys, sample_map):
        assert k == i
    for k, i in zip(keys[:4], sample_map.find_range(None, 5)):
        assert k == i[0]
    for k, i in zip(keys[1:], sample_map.find_range(3, None)):
        assert k == i[0]
    for k, i in zip(keys[1:4], sample_map.find_range(2, 6)):
        assert k == i[0]
    for k, i in zip(keys, sample_map.find_range(None, None)):
        assert k == i[0]

def test_misc(sample_map):
    """Tests miscellaneous inherited methods."""
    root = sample_map.root()
    assert sample_map.parent(root.left()) is root
    assert sample_map.parent(root.right()) is root
    assert sample_map.num_children(root) == 2
    assert sample_map.num_children(root.left()) == 0
