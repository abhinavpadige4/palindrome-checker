"""
Palindrome Checker Module
=========================
Provides functions to check if a string is a palindrome.
Supports case-insensitive checking and ignoring non-alphanumeric characters.
"""


def is_palindrome(s: str, ignore_case: bool = True, ignore_non_alphanumeric: bool = True) -> bool:
    """
    Check if a string is a palindrome.

    A palindrome reads the same forwards and backwards.

    Args:
        s: The string to check.
        ignore_case: If True, 'A' and 'a' are treated as equal. Default True.
        ignore_non_alphanumeric: If True, spaces, punctuation, and symbols are ignored.
                                 Default True.

    Returns:
        True if the string is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("RaceCar", ignore_case=False)
        False
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    cleaned = s

    if ignore_non_alphanumeric:
        cleaned = "".join(ch for ch in cleaned if ch.isalnum())

    if ignore_case:
        cleaned = cleaned.lower()

    return cleaned == cleaned[::-1]


def is_palindrome_two_pointer(s: str, ignore_case: bool = True, ignore_non_alphanumeric: bool = True) -> bool:
    """
    Check if a string is a palindrome using the two-pointer technique.

    This approach is more memory-efficient for very long strings since it
    doesn't create a reversed copy.

    Time Complexity: O(n)
    Space Complexity: O(1) auxiliary (excluding cleaned string)

    Args:
        s: The string to check.
        ignore_case: If True, case is ignored. Default True.
        ignore_non_alphanumeric: If True, non-alphanumeric chars are skipped. Default True.

    Returns:
        True if the string is a palindrome, False otherwise.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric from the left
        if ignore_non_alphanumeric and not s[left].isalnum():
            left += 1
            continue
        # Skip non-alphanumeric from the right
        if ignore_non_alphanumeric and not s[right].isalnum():
            right -= 1
            continue

        left_char = s[left] if not ignore_case else s[left].lower()
        right_char = s[right] if not ignore_case else s[right].lower()

        if left_char != right_char:
            return False

        left += 1
        right -= 1

    return True


def is_palindrome_recursive(s: str, ignore_case: bool = True, ignore_non_alphanumeric: bool = True) -> bool:
    """
    Check if a string is a palindrome using recursion.

    Time Complexity: O(n)
    Space Complexity: O(n) due to recursion stack

    Args:
        s: The string to check.
        ignore_case: If True, case is ignored. Default True.
        ignore_non_alphanumeric: If True, non-alphanumeric chars are ignored. Default True.

    Returns:
        True if the string is a palindrome, False otherwise.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    cleaned = s
    if ignore_non_alphanumeric:
        cleaned = "".join(ch for ch in cleaned if ch.isalnum())
    if ignore_case:
        cleaned = cleaned.lower()

    return _recursive_helper(cleaned, 0, len(cleaned) - 1)


def _recursive_helper(s: str, left: int, right: int) -> bool:
    """Internal recursive helper for palindrome checking."""
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return _recursive_helper(s, left + 1, right - 1)