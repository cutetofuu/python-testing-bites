from lib.string_builder import *

# Initially returns an empty string, when no string is added.

def test_initially_returns_empty_string():
    test_string = StringBuilder()
    assert test_string.output() == ""

# Initially returns a length of zero, when no string is added.

def test_initially_returns_zero_length():
    test_string = StringBuilder()
    assert test_string.size() == 0

# Returns the same string, when one string is added.

def test_returns_same_string_for_one_string():
    test_string = StringBuilder()
    test_string.add("Hello")
    assert test_string.output() == "Hello"

# Returns the correct length, when one string is added.

def test_returns_correct_length_for_one_string():
    test_string = StringBuilder()
    test_string.add("Hello")
    assert test_string.size() == 5

# Returns concatenated strings, when multiple strings are added.

def test_returns_correct_string_for_multiple_strings():
    test_string = StringBuilder()
    test_string.add("Hello ")
    test_string.add("Makers ")
    test_string.add("apprentices!")
    assert test_string.output() == "Hello Makers apprentices!"

# Returns the correct length, when multiple strings are added.

def test_returns_correct_length_for_multiple_strings():
    test_string = StringBuilder()
    test_string.add("Hello ")
    test_string.add("Makers ")
    test_string.add("apprentices!")
    assert test_string.size() == 25