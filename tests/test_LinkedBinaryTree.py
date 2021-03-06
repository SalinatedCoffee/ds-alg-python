import pytest
from src.tree.linkedbinary_tree import linkedbinary_tree

def test_initialization():
    """Test default object instantiation."""
    empty_binary_tree = linkedbinary_tree()
    assert len(empty_binary_tree) == 0
    assert empty_binary_tree.root() is None

def test_add_nodes():
    """Test the appending of nodes to a tree."""
    tree = linkedbinary_tree()
    root = tree._add_root(0)
    assert root.element() == 0
    assert len(tree) == 1
    tree._add_left(root, 1)
    tree._add_right(root, 2)
    assert len(tree) == 3
    assert tree.left(root).element() == 1
    assert tree.right(root).element() == 2
    assert tree.num_children(root) == 2

def generate_basic_tree():
    """Helper function that generates a standard complete binary tree of size 3."""
    tree = linkedbinary_tree()
    root = tree._add_root(0)
    tree._add_left(root, 1)
    tree._add_right(root, 2)
    return tree

def test_remove_nodes():
    """Test the removal of nodes from a tree."""
    tree = generate_basic_tree()
    assert len(tree) == 3
    with pytest.raises(ValueError):
        tree._delete(tree.root())
    for child in tree.children(tree.root()):
        tree._delete(child)
    assert len(tree) == 1
    assert tree._delete(tree.root()) == 0
    assert len(tree) == 0

def test_attach_subtrees():
    """Test the appending of subtrees to a tree."""
    T0 = generate_basic_tree()
    T1 = generate_basic_tree()
    T2 = generate_basic_tree()
    assert len(T0) == len(T1) == len(T2) == 3
    root = T0.root()
    pos = T0.left(root)
    with pytest.raises(ValueError):
        T0._attach(root, T1, T2)
    T0._attach(pos, T1, T2)
    assert len(T0) == len(T0) + len(T1) + len(T2)
