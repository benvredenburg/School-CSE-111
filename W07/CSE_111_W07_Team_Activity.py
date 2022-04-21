from names import given_name, family_name, full_name
import pytest

def test_full_name():
    assert full_name('', '') == ', '
    assert full_name('Bill', '') == ', Bill'
    assert full_name('','Ted') == 'Ted, '
    assert full_name('Mike', 'Smith') == 'Smith, Mike'
    assert full_name('Benjamin', 'Vredenburg') == 'Vredenburg, Benjamin'

def test_given_name():
    assert given_name('Smith, Mike') == 'Mike'
    assert given_name('Vredenburg, Benjamin') == 'Benjamin'

def test_family_name():
    assert family_name('Vredenburg, Benjamin') == 'Vredenburg'
    

pytest.main(['W07/CSE 111 - W07 Team Activity.py'])