import pytest
from palindrome import is_palindrome

def test_is_palindrome():
    assert is_palindrome(767) == print('It is a palindrome')
    assert is_palindrome('MOM') == print('It is a palindrome')
    assert is_palindrome('Mom') == print('It is a palindrome')
    assert is_palindrome('Blue') == print('It is not a palindrome')
    assert is_palindrome(66666669) == print('It is not a palindrome')