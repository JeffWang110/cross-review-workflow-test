#!/usr/bin/env python3
"""
CLI Calculator entry point.
Usage: python -m calculator "1 + 2"
"""

import sys
from calculator.calc import calculate, CalculatorError


def main():
    """Main entry point for CLI calculator."""
    if len(sys.argv) != 2:
        print("Usage: python -m calculator \"<expression>\"")
        print("Example: python -m calculator \"1 + 2\"")
        print("Supported operators: +, -, *, /")
        sys.exit(1)
    
    expression = sys.argv[1]
    
    try:
        result = calculate(expression)
        print(f"{result}")
        sys.exit(0)
    except CalculatorError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()