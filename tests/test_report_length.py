from lib.report_length import *

"""
Reports a length of zero, when passed an empty string.
"""

def test_report_length_returns_zero():
    assert report_length("") == "This string was 0 characters long."

"""
Reports the correct length when passed a single word.
"""

def test_returns_correct_length_for_single_word():
    assert report_length("Hello") == "This string was 5 characters long."

"""
Reports the correct length when passed multiple words.
"""

def test_returns_corrent_length_for_multiple_words():
    assert report_length("Welcome to the Makers bootcamp!") == "This string was 31 characters long."