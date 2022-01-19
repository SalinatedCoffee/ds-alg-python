import pytest
from src.stack.linkedlist_stack import linkedlist_stack
from src.exceptions.PyDSError import StackError

@pytest.fixture(name='empty_stack')
def fixture_empty_stack():
    """pytest fixture for empty stack."""
    return linkedlist_stack()

def test_initialization(empty_stack):
    """Test object initialization."""
    with pytest.raises(StackError.EmptyStack):
        empty_stack.pop()
    assert empty_stack.top() is None
    assert len(empty_stack) == 0

def test_basic_push_pop(empty_stack):
    """Test item push / pop."""
    empty_stack.push(7)
    empty_stack.push(5)
    empty_stack.push(3)
    assert len(empty_stack) == 3
    assert empty_stack.top() == 3
    empty_stack.pop()
    assert empty_stack.pop() == 5
    empty_stack.pop()
    assert empty_stack.top() is None
    assert len(empty_stack) == 0