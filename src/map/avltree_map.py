from src.map.tree_map import tree_map

class avltree_map(tree_map):
    class _Node(tree_map._Node):
        def __init__(self):
            pass

        def left_height(self):
            pass
        
        def right_height(self):
            pass

    def _recompute_height(self, p):
        pass

    def _isbalanced(self, p):
        pass

    def _tall_child(self, p, favorleft=False):
        pass

    def _tall_grandchild(self, p):
        pass

    def _rebalance(self, p):
        pass

    def _rebalance_insert(self, p):
        return super()._rebalance_insert(p)

    def _rebalance_delete(self, p):
        return super()._rebalance_delete(p)
