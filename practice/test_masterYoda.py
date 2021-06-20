import pytest

from masterYoda import master_yoda

def test_master_yoda():
    assert master_yoda('I am good') == 'good am I'
    assert master_yoda('what a beautiful day') == 'day beautiful a what'
    assert master_yoda('Nice to meet you') == 'you meet to Nice'
