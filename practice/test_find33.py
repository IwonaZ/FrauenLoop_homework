import pytest

from find33 import has_33

def test_has_33():
    assert has_33([1, 3, 3]) == True
    assert has_33([1, 3, 1, 3]) == False
    assert has_33([3, 1, 3]) == False