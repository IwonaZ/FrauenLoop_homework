import pytest

from almostThere import almost_there

def test_almostThere():
    assert almost_there(101) == True
    assert almost_there(155) == False
    assert almost_there(207) == True