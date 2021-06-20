import pytest

from spyGame import spy_game

def test_spy_game():
    assert spy_game([1,2,4,0,0,7,5]) == True
    assert spy_game([1,0,2,4,0,5,7]) == True
    assert spy_game([1,7,2,0,4,5,0]) == False