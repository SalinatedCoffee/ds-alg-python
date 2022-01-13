import pytest
from src.LinkedBinaryTree import LinkedBinaryTree

@pytest.fixture(name='empty_binary_tree')
def fixture_empty_binary_tree():
    return LinkedBinaryTree()

def test_initialization(empty_binary_tree):
    assert len(empty_binary_tree) == 0
    assert empty_binary_tree.root() is None
