import pytest

from blackjack import blackjack

def test_blackjack():
    assert blackjack(5,6,7) == 18
    assert blackjack(9,9,9) == 'BUST'
    assert blackjack(9,9,11)== 19
    assert blackjack(3,5,4) == 12
    assert blackjack(11,9,3) == 13