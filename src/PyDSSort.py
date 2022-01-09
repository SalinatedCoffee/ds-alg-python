"""Collection of various sorting algorithms for use with provided data structure implementations."""
from src.PositionalDLList import PositionalDLList

def insertion_sort(L:PositionalDLList) -> None:
    """
    Basic insertion sort algorithm that sorts L in ascending order.
    Assumes that all items in L are comparable with each other.
    """
    if len(L) > 1:
        marker = L.first()
        # until end of list
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            # marker > pivot, already in correct order. Advance marker to pivot
            if value > marker.element():
                marker = pivot
            else:
                walk = marker
                # backtrack from marker towards front of list while comparing values
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                # at this point in time, walk > pivot > walk.prev
                # insert pivot before walk (delete then insert new with pivot.value)
                L.delete(pivot)
                L.add_before(walk, value)
