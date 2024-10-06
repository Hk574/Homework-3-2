""" Module providing a simple calculator with basic arithmetic operations. """
from decimal import Decimal, getcontext
from typing import List, Tuple

# Set precision for Decimal operations
getcontext().prec = 28

class CalculatorError(Exception):
    """Custom exception class for errors related to the Calculator."""

class Calculator:
    """A class to perform basic arithmetic operations and maintain a history of calculations."""
    history: List[Tuple[str, Decimal]] = []

    @classmethod
    def add_to_history(cls, operation: str, result: Decimal) -> None:
        """Adds the result of the calculation to history."""
        cls.history.append((operation, result))

    @classmethod
    def get_last_calculation(cls) -> Tuple[str, Decimal]:
        """Retrieves the last calculation from the history."""
        if not cls.history:
            raise CalculatorError("No calculations in history.")
        return cls.history[-1]

    @classmethod
    def reset_history(cls) -> None:
        """Resets the calculation history."""
        cls.history.clear()

    def add(self, operand1: Decimal, operand2: Decimal) -> Decimal:
        """Adds two Decimal numbers."""
        result = operand1 + operand2
        self.add_to_history(f"{operand1} + {operand2}", result)
        return result

    def subtract(self, operand1: Decimal, operand2: Decimal) -> Decimal:
        """Subtracts the second Decimal number from the first."""
        result = operand1 - operand2
        self.add_to_history(f"{operand1} - {operand2}", result)
        return result

    def multiply(self, operand1: Decimal, operand2: Decimal) -> Decimal:
        """Multiplies two Decimal numbers."""
        result = operand1 * operand2
        self.add_to_history(f"{operand1} * {operand2}", result)
        return result

    def divide(self, operand1: Decimal, operand2: Decimal) -> Decimal:
        """Divides the first Decimal number by the second, raises an error if dividing by zero."""
        if operand2 == 0:
            raise CalculatorError("Cannot divide by zero.")
        result = operand1 / operand2
        self.add_to_history(f"{operand1} / {operand2}", result)
        return result 