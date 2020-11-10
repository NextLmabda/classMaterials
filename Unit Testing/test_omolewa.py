import math_func as mf

def test_product():
    assert mf.product(2, 3) == 6
    assert mf.product(12, 10) == 120
    assert mf.product(12) == 30, f'Omolewa entered function not correct'

def test_add():
    assert mf.add(2, 3) == 5