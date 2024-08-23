# from Terminal > pip install pytest
# from Terminal > pytest .
#
#
import pytest

import calculator

def test_calculator_add_small():
    # Arrange
    x: int = -1
    y: int = 0
    expected: int = -1

    # Act
    actual: int = calculator.add(x, y)

    # Assert
    assert actual == expected

def test_calculator_sub_small():
    # Arrange
    x: int = 14
    y: int = 7
    expected: int = 7

    # Act
    actual: int = calculator.subtract(x, y)

    # Assert
    assert actual == expected

def test_calculator_mul_small():
    # Arrange
    x: int = 8
    y: int = 9
    expected: int = 72

    # Act
    actual: int = calculator.multiply(x, y)

    # Assert
    assert actual == expected

def test_calculator_mul_zero():
    # Arrange
    x: int = 1000
    y: int = 0
    expected: int = 0

    # Act
    actual: int = calculator.multiply(x, y)

    # Assert
    assert actual == expected

def test_calculator_div_small():
    # Arrange
    x: int = 99
    y: int = 11
    expected: int = 9

    # Act
    actual: int = calculator.divide(x, y)

    # Assert
    assert actual == expected

def test_calculator_div_zero_error_phase1():
    # test that we get an error when divide by zero
    # Arrange
    x: int = 99
    y: int = 0

    # Act
    try:
        actual: int = calculator.divide(x, y)
        assert False  # fail the test
    except ZeroDivisionError as e:
        assert True  # pass the test

def test_calculator_div_zero_error_phase2():
    x: int = 99
    y: int = 0
    with pytest.raises(ZeroDivisionError) as ex:
        actual: int = calculator.divide(x, y)

    assert str(ex.value) == "Cannot divide by zero!"

def test_calculator_pow_small():
    x: int = 2;
    y: int = 10;
    expected: float = 1024;

    # Act
    actual: float = calculator.power(x, y);

    # Assert
    assert actual == expected;

def test_calculator_pow_16():
    x: int = 2;
    y: int = 4;
    expected: float = 16;

    # Act
    actual: float = calculator.power(x, y);

    # Assert
    assert actual == expected;

def test_calculator_pow_9():
    x: int = 3;
    y: int = 2;
    expected: float = 9;

    # Act
    actual: float = calculator.power(x, y);

    # Assert
    assert actual == expected;

def test_calculator_pow_zero():
    x: int = 9;
    y: int = 0;
    expected: float = 1;

    # Act
    actual: float = calculator.power(x, y);

    # Assert
    assert actual == expected;

def test_calculator_pow_neg():
    x: int = 2;
    y: int = -2;
    expected: float = 0.25;

    # Act
    actual: float = calculator.power(x, y);

    # Assert
    assert actual == expected;


def test_calculator_pow_neg_div_zero_error():
    x: int = 0
    y: int = -2

    # Act
    try:
        actual: int = calculator.power(x, y)
        assert False  # fail the test
    except ZeroDivisionError as e:
        assert True  # pass the test

    with pytest.raises(ZeroDivisionError) as ex:
        actual: int = calculator.power(x, y)

    assert str(ex.value) == "Cannot divide by zero!"

def test_calculator_sqrt_positive():
    x: int = 25;

    expected: float = 5;

    # Act
    actual: float = calculator.sqrt(x);

    # Assert
    assert actual == expected;

def test_calculator_sqrt_negative():
    x: int = -5;

    try:
        actual: float = calculator.sqrt(x)
        assert False  # fail the test
    except ValueError as e:
        assert True  # pass the test

    with pytest.raises(ValueError) as ex:
        actual = calculator.sqrt(x)

    assert str(ex.value) == "math domain error"

def test_calculator_is_prime_i():
    x: int = 1;

    assert not calculator.is_primary(x);


def test_calculator_is_prime_j():
    x: int = 2;

    assert calculator.is_primary(x);

def test_calculator_is_prime_k():
    x: int = 16;

    assert not calculator.is_primary(x);

def test_calculator_is_prime_l():
    x: int = -3;

    assert not calculator.is_primary(x);

def test_calculator_is_prime_m():
    x: int = 0;

    assert not calculator.is_primary(x);

def test_calculator_factorial_n():
    x: int = 4;

    expected: int = 24;

    # Act
    actual: int = calculator.factorial(x);

    # Assert
    assert actual == expected;

def test_calculator_factorial_o():
    x: int = 0;

    expected: int = 1;

    # Act
    actual: int = calculator.factorial(x);

    # Assert
    assert actual == expected;

def test_calculator_factorial_p():
    x: int = 1;

    expected: int = 1;

    # Act
    actual: int = calculator.factorial(x);

    # Assert
    assert actual == expected;

def test_calculator_factorial_q():
    x: int = 5;

    expected: int = 120;

    # Act
    actual: int = calculator.factorial(x);

    # Assert
    assert actual == expected;

def test_calculator_factorial_r():
    x: int = -3;

    try:
        actual: float = calculator.factorial(x)
        assert False  # fail the test
    except ValueError as e:
        assert True  # pass the test

    with pytest.raises(ValueError) as ex:
        actual = calculator.factorial(x)

    assert str(ex.value) == "factorial not defined for negative values"

test_calculator_pow_small()
test_calculator_pow_16()
test_calculator_pow_9()
test_calculator_pow_zero()
test_calculator_pow_neg()
test_calculator_pow_neg_div_zero_error()
test_calculator_sqrt_positive()
test_calculator_sqrt_negative()
test_calculator_is_prime_i()
test_calculator_is_prime_j()
test_calculator_is_prime_k()
test_calculator_is_prime_l()
test_calculator_is_prime_m()
test_calculator_factorial_n()
test_calculator_factorial_o()
test_calculator_factorial_p()
test_calculator_factorial_q()
test_calculator_factorial_r()




