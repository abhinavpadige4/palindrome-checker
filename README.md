# Palindrome Checker

A comprehensive Python module for checking if strings are palindromes, with multiple implementations and extensive unit tests.

## Features

- **Multiple Implementations**: 
  - Simple slicing approach (`is_palindrome`)
  - Two-pointer technique (`is_palindrome_two_pointer`) 
  - Recursive approach (`is_palindrome_recursive`)
- **Flexible Options**:
  - Case sensitivity control
  - Alphanumeric filtering control
- **Robust Error Handling**: Type checking for input validation
- **Comprehensive Tests**: Full test suite covering edge cases, unicode, and performance
- **Well Documented**: Clear docstrings with examples

## Installation

No installation required - just copy the `palindrome_checker.py` file into your project.

## Usage

```python
from palindrome_checker import is_palindrome, is_palindrome_two_pointer, is_palindrome_recursive

# Basic usage
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False

# With punctuation and spaces
print(is_palindrome("A man, a plan, a canal: Panama"))  # True

# Case sensitive
print(is_palindrome("Racecar", ignore_case=False))  # False

# Keeping non-alphanumeric characters
print(is_palindrome("A man, a plan, a canal: Panama", ignore_non_alphanumeric=False))  # False

# Using different implementations
print(is_palindrome_two_pointer("racecar"))  # True
print(is_palindrome_recursive("racecar"))    # True
```

## Running Tests

To run the unit tests:

```bash
python test_palindrome_checker.py
```

Or using unittest discovery:

```bash
python -m unittest test_palindrome_checker.py -v
```

## Algorithm Details

### Simple Slicing Approach
- **Time Complexity**: O(n)
- **Space Complexity**: O(n) for the cleaned string and its reverse
- **Best for**: Most use cases, readable and concise

### Two-Pointer Technique
- **Time Complexity**: O(n)
- **Space Complexity**: O(1) auxiliary (excluding input)
- **Best for**: Memory-constrained environments or very long strings

### Recursive Approach
- **Time Complexity**: O(n)
- **Space Complexity**: O(n) due to recursion stack
- **Best for**: Educational purposes or when recursion is preferred

## Test Coverage

The test suite includes:
- Basic palindromes and non-palindromes
- Empty strings and single characters
- Strings with punctuation, spaces, and special characters
- Numeric palindromes
- Unicode and emoji support
- Case sensitivity tests
- Error handling for invalid inputs
- Performance tests with long strings
- All three implementation variants

## License

MIT License - feel free to use and modify as needed.