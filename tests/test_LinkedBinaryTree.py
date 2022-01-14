import pytest
from src.LinkedBinaryTree import LinkedBinaryTree

def test_initialization():
    empty_binary_tree = LinkedBinaryTree()
    assert len(empty_binary_tree) == 0
    assert empty_binary_tree.root() is None

def test_add_nodes():
    tree = LinkedBinaryTree()
    root = tree._add_root(0)
    assert root.element() == 0
    assert len(tree) == 1
    tree._add_left(root, 2)
    tree._add_right(root, 3)
    assert len(tree) == 3
    assert tree.left(root).element() == 2
    assert tree.right(root).element() == 3

def generate_basic_tree():
    tree = LinkedBinaryTree()
    root = tree._add_root(0)
    tree._add_left(root, 2)
    tree._add_right(root, 3)
    return tree

def test_remove_nodes():
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
