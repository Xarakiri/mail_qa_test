import pytest


def test_sum():
    number1 = 10.0
    number2 = "test"
    try:
        assert number1 + number2
    except TypeError:
        pass


def test_division():
    number1 = 6.0
    assert number1 / 2 == 3.0


@pytest.mark.parametrize(
    "num1,num2,res",
    [(3.0, 0.0, 0.0),
     (-1.0, -1.0, 1.0),
     (5.0, 5.0, 25.0),
     (-5.0, 5.0, -25.0)]
)
def test_mult(num1, num2, res):
    assert num1 * num2 == res

