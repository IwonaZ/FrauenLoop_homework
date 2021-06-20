import pytest

from paperDoll import paper_doll

def test_paper_doll():
    assert paper_doll('Hello') == 'HHHeeellllllooo'
    assert paper_doll('Mississippi') == 'MMMiiissssssiiissssssiiippppppiii'
    assert paper_doll('Iwona') == 'IIIwwwooonnnaaa'