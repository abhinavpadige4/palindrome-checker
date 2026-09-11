"""
Unit Tests for Palindrome Checker
=================================
Tests all palindrome checking functions with various edge cases.
"""

import unittest
from palindrome_checker import (
    is_palindrome,
    is_palindrome_two_pointer,
    is_palindrome_recursive
)


class TestPalindromeChecker(unittest.TestCase):
    """Test suite for palindrome checking functions."""

    def setUp(self):
        """Set up test cases."""
        self.test_cases = [
            # (input, expected_result, description)
            ("racecar", True, "simple palindrome"),
            ("hello", False, "simple non-palindrome"),
            ("", True, "empty string"),
            ("a", True, "single character"),
            ("aa", True, "two same characters"),
            ("ab", False, "two different characters"),
            ("A man, a plan, a canal: Panama", True, "classic palindrome with punctuation"),
            ("No lemon, no melon", True, "palindrome with spaces and comma"),
            ("Was it a car or a cat I saw?", True, "question palindrome"),
            ("race a car", False, "almost palindrome"),
            ("12321", True, "numeric palindrome"),
            ("12345", False, "numeric non-palindrome"),
            ("123abc321", True, "alphanumeric palindrome"),
            ("123abccba321", True, "complex alphanumeric palindrome"),
            ("Madam, I'm Adam", True, "palindrome with apostrophe and comma"),
            ("", True, "empty string edge case"),
            ("   ", True, "whitespace only (ignored)"),
            ("A", True, "single uppercase"),
            ("a", True, "single lowercase"),
            ("0P", False, "mixed alphanumeric case-sensitive"),
        ]

    def test_is_palindrome_basic(self):
        """Test the main is_palindrome function."""
        for input_str, expected, description in self.test_cases:
            with self.subTest(input=input_str, description=description):
                result = is_palindrome(input_str)
                self.assertEqual(result, expected, 
                               f"Failed for '{input_str}' ({description})")

    def test_is_palindrome_case_sensitive(self):
        """Test is_palindrome with case sensitivity."""
        # These should be False when case-sensitive
        case_sensitive_false = [
            "Racecar",
            "Madam",
            "A man, a plan, a canal: Panama"
        ]
        
        for input_str in case_sensitive_false:
            with self.subTest(input=input_str):
                result = is_palindrome(input_str, ignore_case=False)
                self.assertFalse(result, 
                               f"Should be False when case-sensitive for '{input_str}'")
        
        # These should be True even when case-sensitive (already same case)
        case_sensitive_true = [
            "racecar",
            "madam",
            "12321"
        ]
        
        for input_str in case_sensitive_true:
            with self.subTest(input=input_str):
                result = is_palindrome(input_str, ignore_case=False)
                self.assertTrue(result, 
                              f"Should be True when case-sensitive for '{input_str}'")

    def test_is_palindrome_keep_non_alphanumeric(self):
        """Test is_palindrome when keeping non-alphanumeric characters."""
        # These should be False when we don't ignore non-alphanumeric
        keep_chars_false = [
            "A man, a plan, a canal: Panama",  # has spaces, comma, colon
            "race car",  # has space
            "hello!"  # has exclamation
        ]
        
        for input_str in keep_chars_false:
            with self.subTest(input=input_str):
                result = is_palindrome(input_str, ignore_non_alphanumeric=False)
                self.assertFalse(result, 
                               f"Should be False when keeping non-alphanumeric for '{input_str}'")
        
        # These should be True even when keeping non-alphanumeric (they're symmetric)
        keep_chars_true = [
            "a!a",  # symmetric with punctuation
            "ab ba",  # symmetric with space
            "123!@#321"  # symmetric with special chars
        ]
        
        for input_str in keep_chars_true:
            with self.subTest(input=input_str):
                result = is_palindrome(input_str, ignore_non_alphanumeric=False)
                self.assertTrue(result, 
                              f"Should be True when keeping non-alphanumeric for '{input_str}'")

    def test_is_palindrome_two_pointer(self):
        """Test the two-pointer implementation."""
        for input_str, expected, description in self.test_cases:
            with self.subTest(input=input_str, description=description):
                result = is_palindrome_two_pointer(input_str)
                self.assertEqual(result, expected, 
                               f"Two-pointer failed for '{input_str}' ({description})")

    def test_is_palindrome_recursive(self):
        """Test the recursive implementation."""
        for input_str, expected, description in self.test_cases:
            with self.subTest(input=input_str, description=description):
                result = is_palindrome_recursive(input_str)
                self.assertEqual(result, expected, 
                               f"Recursive failed for '{input_str}' ({description})")

    def test_error_handling(self):
        """Test error handling for invalid inputs."""
        invalid_inputs = [None, 123, [], {}, 12.34]
        
        for invalid_input in invalid_inputs:
            with self.subTest(input=invalid_input):
                # Test all three functions
                for func in [is_palindrome, is_palindrome_two_pointer, is_palindrome_recursive]:
                    with self.assertRaises(TypeError):
                        func(invalid_input)

    def test_performance_long_string(self):
        """Test performance with a long string."""
        # Create a long palindrome
        long_palindrome = "a" * 10000 + "b" + "a" * 10000
        long_non_palindrome = "a" * 10000 + "bc" + "a" * 10000
        
        # These should not hang or crash
        self.assertTrue(is_palindrome(long_palindrome))
        self.assertFalse(is_palindrome(long_non_palindrome))
        
        # Test with two-pointer as well
        self.assertTrue(is_palindrome_two_pointer(long_palindrome))
        self.assertFalse(is_palindrome_two_pointer(long_non_palindrome))

    def test_unicode_characters(self):
        """Test with unicode characters."""
        unicode_tests = [
            ("🎂🎉🎂", True, "emoji palindrome"),
            ("🎂🎉🎃", False, "emoji non-palindrome"),
            ("абба", True, "cyrillic palindrome"),  # Russian: abba
            ("абвг", False, "cyrillic non-palindrome"),
        ]
        
        for input_str, expected, description in unicode_tests:
            with self.subTest(input=input_str, description=description):
                result = is_palindrome(input_str)
                self.assertEqual(result, expected, 
                               f"Unicode test failed for '{input_str}' ({description})")


if __name__ == "__main__":
    # Run the tests
    unittest.main(verbosity=2)