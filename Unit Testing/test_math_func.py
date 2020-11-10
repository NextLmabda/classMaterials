import math_func as mf
import pytest

#@pytest.mark.numbers
def test_product():
    assert mf.product(2, 3) == 6
    assert mf.product(12, 10) == 120
    assert mf.product(12) == 24, f'Omolewa entered function not correct'

#@pytest.mark.numbers
def test_add():
    assert mf.add(2, 3) == 5

#@pytest.mark.strings
def test_add_string():
    result = mf.add('Hello', 'World')
    assert result == 'HelloWorld'
    assert type(result) == str
    assert 'Heldlo' not in result

@pytest.mark.parametrize
#@pytest.mark.strings
def test_product_string():
    assert mf.product('Hello ', 3) == 'Hello Hello Hello '
    result = mf.product('Hello ')
    assert result == 'Hello Hello '
    #assert len(result) == 11
    assert type(result) is str
    assert 'Hello' in result

