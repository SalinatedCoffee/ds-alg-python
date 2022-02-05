import pytest
from src.map.chain_hashmap import chain_hashmap

@pytest.fixture(name='empty_hashmap')
def fixture_empty_hashmap():
    """pytest fixture that generates an empty chain_hashmap object."""
    return chain_hashmap()

@pytest.fixture(name='sample_hashmap')
def fixture_sample_hashmap():
    """
    pytest fixture that generates a populated chain_hashmap object.
    For default parameters for src.map.hashmap.__init__(), resizing will not occur.
    """
    tuples = [(0, "Zero"), (1, "One"), (2, "Two"), (3, "Three"), (4, "Four")]
    ret = chain_hashmap()
    for (k, v) in tuples:
        ret[k] = v
    if len(ret) != len(tuples):
        raise Exception('Failed to construct correct hash map')
    return ret

def test_intialization(empty_hashmap):
    """Tests object instantiation."""
    assert len(empty_hashmap) == 0
    with pytest.raises(KeyError):
        del empty_hashmap[123]

def test_add_items(empty_hashmap):
    """Tests the addition of new key-value pairs."""
    empty_hashmap[0] = "Zero"
    assert len(empty_hashmap) == 1
    empty_hashmap[1] = "One"
    empty_hashmap[2] = "Two"
    assert len(empty_hashmap) == 3

def test_mutate_items(sample_hashmap):
    """Tests the mutation of the value of a given key."""
    sample_hashmap[1] = "Uno"
    assert sample_hashmap[1] == "Uno"

def test_remove_items(sample_hashmap):
    """Tests the removal of key-value pairs."""
    init = len(sample_hashmap)
    del sample_hashmap[0]
    assert len(sample_hashmap) == init - 1
    with pytest.raises(KeyError):
        sample_hashmap[0]
    del sample_hashmap[1]
    del sample_hashmap[2]
    assert len(sample_hashmap) == init - 3

def test_internal_resize(sample_hashmap):
    """
    Tests the internal resize method; assumes default parameters where
    Load factor = 0.5
    Size scaling = 2
    """
    init = len(sample_hashmap)
    # Trigger first resize
    for i in range(5, 10):
        sample_hashmap[i] = str(i)
    assert sample_hashmap[0] == "Zero"
    assert sample_hashmap[4] == "Four"
    assert sample_hashmap[5] == '5'
    assert sample_hashmap[9] == '9'
    # Trigger second resize
    for i in range(10, 15):
        sample_hashmap[i] = str(i)
    assert sample_hashmap[0] == "Zero"
    assert sample_hashmap[4] == "Four"
    assert sample_hashmap[5] == '5'
    assert sample_hashmap[9] == '9'
    assert sample_hashmap[10] == '10'
    assert sample_hashmap[14] == '14'
    assert len(sample_hashmap) == init + 10
