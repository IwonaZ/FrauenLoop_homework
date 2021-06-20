import pytest

from summer69 import summer_69

def test_summer69():
    assert summer_69([1,3,5]) == 9
    assert summer_69([4,5,6,7,8,9]) == 9
    assert summer_69([2,1,6,9,11]) == 14