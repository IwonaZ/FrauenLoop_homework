import pytest
from oldMacdonald import old_mcdonald


def test_oldMacdonald():
    assert old_mcdonald('macdonald') == 'MacDonald'
    assert old_mcdonald('iwona') == 'IwoNa'
    assert old_mcdonald('Butterfly') == 'ButTerfly'