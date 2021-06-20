import pytest

from rangeCheck import ran_check

def test_ran_check():
    assert ran_check(8,2,7) == print('8 is not in the range between 2 and 7')
    assert ran_check(1,2,5) == print('1 is not in the range between 2 and 5')
    assert ran_check(4,4,5) == print('4 is in the range between 4 and 5')