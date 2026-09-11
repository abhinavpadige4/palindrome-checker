"""
Palindrome Checker Module
=========================

Provides a function to check if an input (string or integer) is a palindrome.
Handles string inputs (case-insensitive, ignores non-alphanumeric) and integer inputs.
"""


def is_palindrome(input_value) -> bool:
    """
    Check if input is a palindrome.
    
    A palindrome reads the same forwards and backwards.
    
    Args:
        input_value: String or integer to check.
        
    Returns:
        True if the input is a palindrome, False otherwise.
        
    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome(12321)
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome(12345)
        False
    """
    # Handle None input
    if input_value is None:
        return False
    
    # Convert input to string for uniform processing
    s = str(input_value)
    
    # Normalize: keep only alphanumeric characters and convert to lowercase
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    
    # Check if cleaned string equals its reverse
    return cleaned == cleaned[::-1]