import pytest
from decimal import Decimal
from calculator.calculator import Calculator, CalculatorError

@pytest.fixture
def calculator():
    """Fixture that returns a new Calculator instance."""
    return Calculator()

def test_add(calculator):
    assert calculator.add(Decimal('2'), Decimal('3')) == Decimal('5')
    assert calculator.add(Decimal('-1'), Decimal('1')) == Decimal('0')

def test_subtract(calculator):
    assert calculator.subtract(Decimal('5'), Decimal('3')) == Decimal('2')
    assert calculator.subtract(Decimal('0'), Decimal('5')) == Decimal('-5')

def test_multiply(calculator):
    assert calculator.multiply(Decimal('4'), Decimal('3')) == Decimal('12')
    assert calculator.multiply(Decimal('-2'), Decimal('3')) == Decimal('-6')

def test_divide(calculator):
    assert calculator.divide(Decimal('10'), Decimal('2')) == Decimal('5')
    with pytest.raises(CalculatorError, match="Cannot divide by zero."):
        calculator.divide(Decimal('10'), Decimal('0'))

def test_history(calculator):
    calculator.add(Decimal('2'), Decimal('3'))
    calculator.subtract(Decimal('5'), Decimal('2'))
    last_calc = calculator.get_last_calculation()
    assert last_calc == ("5 - 2", Decimal('3'))

def test_reset_history(calculator):
    calculator.add(Decimal('1'), Decimal('2'))
    Calculator.reset_history()  
    with pytest.raises(CalculatorError, match="No calculations in history."):
        calculator.get_last_calculation()

def test_class_method():
    calc = Calculator()
    calc.add(Decimal('2'), Decimal('2'))
    assert Calculator.get_last_calculation() == ("2 + 2", Decimal('4'))

def test_static_method_create_instance():
    calc = Calculator.create_instance()
    assert isinstance(calc, Calculator)
    assert calc.add(Decimal('1'), Decimal('1')) == Decimal('2')