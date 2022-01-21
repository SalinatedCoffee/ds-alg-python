# TODO: Implement iterative versions of tree traversal functions
"""Collection of various tree / graph traversal algorithms."""
import src.tree.linkedbinary_tree as linkedbinary_tree

def inorder(tree:linkedbinary_tree):
    """Starting from the root, performs an inorder traversal of the tree."""
    # L -> N -> R
    if len(tree):
        for n in _inorder_helper(tree, tree.root()):
            yield n

def _inorder_helper(tree, p):
    """Helper function for inorder()."""
    if tree.left(p):
        for n in _inorder_helper(tree, tree.left(p)):
            yield n
    yield p
    if tree.right(p):
        for n in _inorder_helper(tree, tree.right(p)):
            yield n

def postorder(tree:linkedbinary_tree):
    """Starting from the root, performs a postorder traversal of the tree."""
    # L -> R -> N
    if len(tree):
        for n in _postorder_helper(tree, tree.root()):
            yield n

def _postorder_helper(tree, p):
    """Helper function for postorder()."""
    for n in tree.children(p):
        for i in _postorder_helper(tree, n):
            yield i
    yield p

def preorder(tree:linkedbinary_tree):
    """Starting from the root, performs a preorder traversal of the tree."""
    # N -> L -> R
    if len(tree):
        for n in _preorder_helper(tree, tree.root()):
            yield n

def _preorder_helper(tree, p):
    """Helper function for preorder()."""
    yield p
    for n in tree.children(p):
        for i in _preorder_helper(tree, n):
            yield i
