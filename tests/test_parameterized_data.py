import pytest
from decimal import Decimal
from calculator.calculator import Calculator, CalculatorError

@pytest.fixture
def calculator():
    """Fixture that returns a new Calculator instance."""
    return Calculator()

# Parameterized test for addition
@pytest.mark.parametrize("operand1, operand2, expected", [
    (Decimal('2'), Decimal('3'), Decimal('5')),
    (Decimal('-1'), Decimal('1'), Decimal('0')),
    (Decimal('0'), Decimal('0'), Decimal('0')),
    (Decimal('-2.5'), Decimal('3.5'), Decimal('1.0'))
])
def test_add(calculator, operand1, operand2, expected):
    assert calculator.add(operand1, operand2) == expected

# Parameterized test for subtraction
@pytest.mark.parametrize("operand1, operand2, expected", [
    (Decimal('5'), Decimal('3'), Decimal('2')),
    (Decimal('0'), Decimal('5'), Decimal('-5')),
    (Decimal('7.5'), Decimal('2.5'), Decimal('5.0')),
    (Decimal('-3'), Decimal('-3'), Decimal('0'))
])
def test_subtract(calculator, operand1, operand2, expected):
    assert calculator.subtract(operand1, operand2) == expected

# Parameterized test for multiplication
@pytest.mark.parametrize("operand1, operand2, expected", [
    (Decimal('4'), Decimal('3'), Decimal('12')),
    (Decimal('-2'), Decimal('3'), Decimal('-6')),
    (Decimal('0'), Decimal('5'), Decimal('0')),
    (Decimal('-2'), Decimal('-2'), Decimal('4'))
])
def test_multiply(calculator, operand1, operand2, expected):
    assert calculator.multiply(operand1, operand2) == expected

# Parameterized test for division
@pytest.mark.parametrize("operand1, operand2, expected", [
    (Decimal('10'), Decimal('2'), Decimal('5')),
    (Decimal('9'), Decimal('3'), Decimal('3')),
    (Decimal('5'), Decimal('0.5'), Decimal('10')),
    (Decimal('-6'), Decimal('2'), Decimal('-3'))
])
def test_divide(calculator, operand1, operand2, expected):
    assert calculator.divide(operand1, operand2) == expected

def test_divide_by_zero(calculator):
    """Test that dividing by zero raises the appropriate error."""
    with pytest.raises(CalculatorError, match="Cannot divide by zero."):
        calculator.divide(Decimal('10'), Decimal('0'))
