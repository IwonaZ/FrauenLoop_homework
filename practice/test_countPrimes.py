import pytest

from countPrimes import count_primes

def test_count_primes():
    assert count_primes(100) == 25