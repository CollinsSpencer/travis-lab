import pytest
from util import add, sub

def test_add():
    assert add(1, 2) == 3, "test failed"

def test_sub():
    assert sub(5, 2) == 3, "test failed"
