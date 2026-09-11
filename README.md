# Palindrome Checker

A simple Python function to check if a string or integer is a palindrome.

## Features

- Handles both string and integer inputs
- Case-insensitive for string inputs
- Ignores non-alphanumeric characters in strings
- Works with Unicode characters
- Comprehensive unit test suite

## Installation

No installation required beyond Python 3.8+. The module uses only built-in functions.

## Usage

```python
from palindrome import is_palindrome

# String palindromes
print(is_palindrome("racecar"))  # True
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("hello"))  # False

# Integer palindromes
print(is_palindrome(12321))  # True
print(is_palindrome(12345))  # False

# Edge cases
print(is_palindrome(""))  # True (empty string)
print(is_palindrome("a"))  # True (single character)
print(is_palindrome("!!!"))  # True (only non-alphanumeric)
```

## Running Tests

To run the unit tests:

```bash
# Using unittest (built-in)
python -m unittest test_palindrome.py

# Or run the test file directly
python test_palindrome.py
```

## Function Specification

### `is_palindrome(input_value) -> bool`

**Parameters:**
- `input_value`: Any value that can be converted to string (str, int, float, etc.)

**Returns:**
- `True` if the input is a palindrome, `False` otherwise

**Behavior:**
1. Converts input to string using `str()`
2. Filters to keep only alphanumeric characters (`isalnum()`)
3. Converts to lowercase for case-insensitive comparison
4. Checks if the cleaned string equals its reverse

**Examples:**
- `is_palindrome("A man, a plan, a canal: Panama")` → `True`
- `is_palindrome(12321)` → `True`
- `is_palindrome("hello")` → `False`
- `is_palindrome("")` → `True`
- `is_palindrome(None)` → `False`

## Test Coverage

The test suite includes:
- Basic string palindromes
- Case sensitivity tests
- Punctuation and whitespace handling
- Integer palindromes
- Edge cases (empty string, single char, etc.)
- Invalid input handling
- Unicode character support

## License

MIT