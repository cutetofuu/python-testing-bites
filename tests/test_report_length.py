from lib.report_length import *

def test_report_length_returns_correct_length():
    assert report_length("") == "This string was 0 characters long."
    assert report_length("Hello world!") == "This string was 12 characters long."
    assert report_length("Welcome to the Makers bootcamp!") == "This string was 31 characters long."