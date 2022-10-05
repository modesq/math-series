from functions.series import fibonacci
from functions.series import lucas_series
from functions.series import sum_series


"""
the param(n) for the nth is mandatory for all functions 
optional params = (0, 1) or (no params) => fibonacci()
optional params = (2, 1) or (1, 2) => lucas()
optional params = (anyhting else) => sum_series()
"""

# testing fibonacci function
def test_fibonacci_positive_param():  # with a positive parameter
    actual = fibonacci(10)
    excepted = 55
    assert actual == excepted


def test_fibonacci_negative_param():  # with a negative parameter
    actual = fibonacci(-10)
    excepted = -55
    assert actual == excepted


def test_fibonacci_zero_param():  # with 0 as the parameter
    actual = fibonacci(0)
    excepted = 0
    assert actual == excepted


# ----------------------------------------------------------------

# testing lucas_series function
def test_lucas_series_positive_param():  # with a positive parameter
    actual = lucas_series(10)
    excepted = 123
    assert actual == excepted


def test_lucas_series_negative_param():  # with a negative parameter
    actual = lucas_series(-10)
    excepted = -123
    assert actual == excepted


def test_lucas_series_zero_param():  # with 0 as the parameter
    actual = lucas_series(0)
    excepted = 2
    assert actual == excepted


# ----------------------------------------------------------------

# testing sum_series function
def test_sum_series_1():  # with only the required parameter (will call fibonacci)
    actual = sum_series(10)
    excepted = 55
    assert actual == excepted


def test_sum_series_2():  # with 1 and 2 as optional parameters (will call lucas_series)
    actual = sum_series(10, 2, 1)
    excepted = 123
    assert actual == excepted


def test_sum_series_3():  # with random positive numbers as optional parameters
    actual = sum_series(4, 3, 4)
    excepted = 11
    assert actual == excepted


def test_sum_series_4():  # with random negative numbers as optional parameters
    actual = sum_series(4, -3, -4)
    excepted = -11
    assert actual == excepted
