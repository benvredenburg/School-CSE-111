import pytest
from words import prefix, suffix

def test_prefix():
    a = 'inconceivable'
    b = 'inconvenient'
    p = prefix(a, b)
    assert p == 'incon'

pytest.main(['test_words.py'])