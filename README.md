# Data Structures and Algorithms in Python

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)  
[![pytest](https://github.com/SalinatedCoffee/ds-alg-python/actions/workflows/python-package.yml/badge.svg?event=push)](https://github.com/SalinatedCoffee/ds-alg-python/actions/workflows/python-package.yml)

Implementation of various data structures as described in the book [Data Structures and Algorithms in Python (1st edition)](https://www.amazon.com/Structures-Algorithms-Python-Michael-Goodrich/dp/1118290275/ref=sr_1_6?crid=27YET3X37F0LB), for fun and profit.  
Most(if not all) modules have corresponding unit tests. If you(for some reason) want to use this package in your own code, simply clone the repository and import the package as you would any other.  

### File Structure

```txt
.
├── LICENSE
├── README.md
├── src
│   ├── __init__.py
│   ├── algo
│   │   ├── __init__.py
│   │   ├── sort.py
│   │   └── traverse.py
│   ├── exceptions
│   │   ├── PyDSError.py
│   │   └── __init__.py
│   ├── list
│   │   ├── __init__.py
│   │   ├── doublylinked_list.py
│   │   └── positional_list.py
│   ├── map
│   │   ├── __init__.py
│   │   ├── avltree_map.py
│   │   ├── chain_hashmap.py
│   │   ├── hashmap.py
│   │   ├── linear_hashmap.py
│   │   ├── map.py
│   │   ├── sorted_map.py
│   │   ├── tree_map.py
│   │   └── unsorted_map.py
│   ├── queue
│   │   ├── __init__.py
│   │   ├── arraycircular_deque.py
│   │   ├── arraycircular_queue.py
│   │   ├── circularlinked_queue.py
│   │   ├── doublylinked_deque.py
│   │   ├── heap_pqueue.py
│   │   ├── linkedlist_queue.py
│   │   ├── priority_queue.py
│   │   ├── sorted_pqueue.py
│   │   └── unsorted_pqueue.py
│   ├── stack
│   │   ├── __init__.py
│   │   └── linkedlist_stack.py
│   └── tree
│       ├── __init__.py
│       ├── binary_tree.py
│       ├── linkedbinary_tree.py
│       └── tree.py
└── tests
    ├── __init__.py
    ├── test_ArrayCircularDeque.py
    ├── test_ArrayCircularQueue.py
    ├── test_ChainedHashMap.py
    ├── test_CircularLLQueue.py
    ├── test_DoublyLinkedDeque.py
    ├── test_DoublyLinkedList.py
    ├── test_FloydWarshall.py
    ├── test_HeapPQueue.py
    ├── test_LinearHashMap.py
    ├── test_LinkedBinaryTree.py
    ├── test_LinkedListQueue.py
    ├── test_LinkedListStack.py
    ├── test_PositionalDLList.py
    ├── test_PyDSSort.py
    ├── test_SortedMap.py
    ├── test_SortedPQueue.py
    ├── test_TreeMap.py
    ├── test_UnsortedMap.py
    └── test_UnsortedPQueue.py
```