import pytest
from calc.calculator import add, sub, mul, div


def test_add():
    assert add(2, 5) == 7


def test_sub():
    assert sub(7, 4) == 3


def test_mul():
    assert mul(5, 5) == 25


def test_div():
    assert div(16, 4) == 4


def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(5, 0)
