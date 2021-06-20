import pytest

from pangram import ispangram

def test_ispangram():
    assert ispangram("The quick brown fox jumps over the lazy dog") == True
    assert ispangram("Hello World") == False
