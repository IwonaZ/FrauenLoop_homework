import pytest

from palindrome import palindrome

def test_palindrome():
    assert palindrome('madam') == True
    assert palindrome('kayak') == True
    assert palindrome('nurses run') == True
    assert palindrome('Hello') == False
    assert palindrome("I am happy") == False


