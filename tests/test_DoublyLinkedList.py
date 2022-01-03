import pytest
from src.DoublyLinkedList import DoublyLinkedList

@pytest.fixture(name='basic_dll')
def fixture_basic_dll():
    temp = DoublyLinkedList()
    return temp
