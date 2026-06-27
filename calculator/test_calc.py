"""
Unit tests for calculator module.
Run with: pytest calculator/test_calc.py -v
"""

import pytest
from calculator.calc import (
    add,
    subtract,
    multiply,
    divide,
    calculate,
    parse_expression,
    DivisionByZeroError,
    InvalidInputError,
)


class TestBasicOperations:
    """Test basic arithmetic operations."""
    
    def test_add(self):
        assert add(1, 2) == 3
        assert add(0, 0) == 0
        assert add(-1, 1) == 0
        assert add(1.5, 2.5) == 4.0
    
    def test_subtract(self):
        assert subtract(5, 3) == 2
        assert subtract(0, 0) == 0
        assert subtract(1, 5) == -4
        assert subtract(5.5, 0.5) == 5.0
    
    def test_multiply(self):
        assert multiply(2, 3) == 6
        assert multiply(0, 100) == 0
        assert multiply(-2, 3) == -6
        assert multiply(2.5, 4) == 10.0
    
    def test_divide(self):
        assert divide(6, 2) == 3
        assert divide(1, 2) == 0.5
        assert divide(-6, 2) == -3
        assert divide(10, 4) == 2.5
    
    def test_divide_by_zero(self):
        with pytest.raises(DivisionByZeroError):
            divide(1, 0)


class TestParseExpression:
    """Test expression parsing."""
    
    def test_parse_addition(self):
        left, op, right = parse_expression("1 + 2")
        assert left == 1
        assert op == "+"
        assert right == 2
    
    def test_parse_subtraction(self):
        left, op, right = parse_expression("10 - 3")
        assert left == 10
        assert op == "-"
        assert right == 3
    
    def test_parse_multiplication(self):
        left, op, right = parse_expression("5 * 4")
        assert left == 5
        assert op == "*"
        assert right == 4
    
    def test_parse_division(self):
        left, op, right = parse_expression("8 / 2")
        assert left == 8
        assert op == "/"
        assert right == 2
    
    def test_parse_floats(self):
        left, op, right = parse_expression("3.5 + 2.5")
        assert left == 3.5
        assert op == "+"
        assert right == 2.5
    
    def test_parse_negative_numbers(self):
        # Note: "-5 + 3" has "-" at position 0, should skip it
        left, op, right = parse_expression("5 + -3")
        assert left == 5
        assert op == "+"
        assert right == -3
    
    def test_parse_no_spaces(self):
        left, op, right = parse_expression("1+2")
        assert left == 1
        assert op == "+"
        assert right == 2
    
    def test_parse_invalid_no_operator(self):
        with pytest.raises(InvalidInputError):
            parse_expression("123")
    
    def test_parse_invalid_format(self):
        with pytest.raises(InvalidInputError):
            parse_expression("+ 2")


class TestCalculate:
    """Test full calculation functionality."""
    
    def test_calculate_addition(self):
        assert calculate("1 + 2") == 3
    
    def test_calculate_subtraction(self):
        assert calculate("10 - 3") == 7
    
    def test_calculate_multiplication(self):
        assert calculate("5 * 4") == 20
    
    def test_calculate_division(self):
        assert calculate("8 / 2") == 4
    
    def test_calculate_float_result(self):
        assert calculate("1 / 2") == 0.5
    
    def test_calculate_division_by_zero(self):
        with pytest.raises(DivisionByZeroError):
            calculate("1 / 0")
    
    def test_calculate_invalid_expression(self):
        with pytest.raises(InvalidInputError):
            calculate("abc + def")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])