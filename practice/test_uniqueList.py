import pytest

from uniqueList import unique_list

def test_unique_list():
    assert unique_list([1,1,1,1,2,2,3,3,3,3,4,5]) == [1, 2, 3, 4, 5]
    assert unique_list([1,2,2,3,3,3,3,4,5,6,7,9,15]) == [1, 2, 3, 4, 5, 6, 7, 9, 15]
    assert unique_list([9,9,21,4,4,6,6,6,5]) == [9, 21, 4, 6, 5]