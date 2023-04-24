from lib.check_codeword import *

def test_check_codeword_returns_correct_for_horse():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword_returns_close_for_hope_and_house():
    assert check_codeword("hope") == "Close, but nope."
    assert check_codeword("house") == "Close, but nope."

def test_check_codeword_returns_wrong_for_other_animals():
    assert check_codeword("cat") == "WRONG!"
    assert check_codeword("otter") == "WRONG!"