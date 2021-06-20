import pytest

from volumeOfSphere import vol

def test_vol():
    assert vol(2) == 33.510321638291124
    assert vol(5) == 523.5987755982989
    assert vol(1.5) == 14.137166941154067