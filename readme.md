# TDD Calculator

A simple calculator implemented in Python using Test-Driven Development (TDD) principles.

## Files

- [`calculator.py`](calculator.py): Contains functions for adding numbers from strings with various delimiters and rules.
- [`test.py`](test.py): Unit tests for the calculator functions using Python's `unittest` framework.

## Usage

### Calculator Functions

- `add(inputStr: str)`: Adds numbers separated by commas in a string.
- `addNewLine(inputStr: str)`: Adds numbers separated by commas or new lines.
- `addAllowDelimiters(inputStr: str)`: Adds numbers separated by a custom delimiter specified in the string.
- `addDisallowNegative(inputStr: str)`: Adds numbers separated by a custom delimiter, raises an exception if negative numbers are present.

### Running Tests

To run the unit tests, execute:

```sh
python -m unittest test.py
```

## Example

```python
from calculator import add, addNewLine, addAllowDelimiters, addDisallowNegative

print(add("1,2,3"))                # Output: 6
print(addNewLine("1\n2,3"))        # Output: 6
print(addAllowDelimiters("//;\n1;2"))  # Output: 3

try:
    addDisallowNegative("//;\n1;-2")
except Exception as e:
    print(e)  # Output: negative numbers not allowed -2
```
