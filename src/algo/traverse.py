# TODO: Implement iterative versions of tree traversal functions
"""Collection of various tree / graph traversal algorithms."""
from typing import List, Tuple
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

def floydwarshall(adj:List[List[Tuple[int,int]]]):
    """
    Given an adjacency list, runs the Floyd-Warshal algorithm on the graph represented by it.
    The graph MUST NOT contain any negative cycles.
    Returns the cost matrix of all nodes.
    """
    m = len(adj)
    # initialize cost matrix
    cost = [[float('inf')]*m for _ in range(m)]
    for i in range(m):
        for d, c in adj[i]:
            cost[i][d] = c
    for i in range(m):
        cost[i][i] = 0
    
    for i in range(m):
        for j in range(m):
            for k in range(m):
                if cost[j][k] > cost[j][i] + cost[i][k]:
                    cost[j][k] = cost[j][i] + cost[i][k]
    
    return cost
