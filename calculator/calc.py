"""
Calculator core logic module.
Supports basic arithmetic operations: +, -, *, /
"""


class CalculatorError(Exception):
    """Base exception for calculator errors."""
    pass


class DivisionByZeroError(CalculatorError):
    """Raised when attempting to divide by zero."""
    pass


class InvalidInputError(CalculatorError):
    """Raised when input is invalid."""
    pass


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """
    Divide a by b.
    
    Raises:
        DivisionByZeroError: If b is zero.
    """
    if b == 0:
        raise DivisionByZeroError("Cannot divide by zero")
    return a / b


OPERATORS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def parse_expression(expression: str) -> tuple[float, str, float]:
    """
    Parse a mathematical expression string.
    
    Format: "<number> <operator> <number>"
    Example: "1 + 2" or "3.5 * 4"
    
    Args:
        expression: The expression string to parse.
        
    Returns:
        A tuple of (left_operand, operator, right_operand).
        
    Raises:
        InvalidInputError: If the expression cannot be parsed.
    """
    expression = expression.strip()
    
    # Find operator position
    operator = None
    operator_pos = -1
    
    for op in OPERATORS.keys():
        pos = expression.find(op)
        if pos != -1:
            # Handle negative numbers at the start
            if op == '-' and pos == 0:
                # Skip the leading '-' but continue searching for other operators
                # Including other '-' signs that appear later in the expression
                next_pos = expression.find('-', pos + 1)
                if next_pos != -1:
                    if operator_pos == -1 or next_pos < operator_pos:
                        operator = '-'
                        operator_pos = next_pos
                continue
            if operator_pos == -1 or pos < operator_pos:
                operator = op
                operator_pos = pos
    
    if operator is None:
        raise InvalidInputError(f"No valid operator found in expression: {expression}")
    
    try:
        left_str = expression[:operator_pos].strip()
        right_str = expression[operator_pos + 1:].strip()
        
        if not left_str or not right_str:
            raise InvalidInputError(f"Invalid expression format: {expression}")
        
        left = float(left_str)
        right = float(right_str)
        
        return left, operator, right
        
    except ValueError as e:
        raise InvalidInputError(f"Invalid number in expression: {expression}") from e


def calculate(expression: str) -> float:
    """
    Calculate the result of a mathematical expression.
    
    Args:
        expression: A string expression like "1 + 2" or "3.5 * 4"
        
    Returns:
        The result of the calculation.
        
    Raises:
        InvalidInputError: If the expression is invalid.
        DivisionByZeroError: If attempting to divide by zero.
    """
    left, operator, right = parse_expression(expression)
    operation = OPERATORS[operator]
    return operation(left, right)