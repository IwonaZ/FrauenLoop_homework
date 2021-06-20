import pytest

from multiplyList import multiply

def test_multiply():
    assert multiply([1,2,3,-4]) == -24
    assert multiply([1,5,5,10]) == 250
    assert multiply([6,4,-9,-12]) == 2592