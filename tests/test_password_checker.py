import pytest
from lib.password_checker import *

# Returns True if given password has a length of 8

def test_returns_true_for_password_length_of_eight():
    test_checker = PasswordChecker()
    assert test_checker.check("password") == True

# Returns True if given password has a length of greater than 8

def test_returns_true_for_password_length_of_greater_than_eight():
    test_checker = PasswordChecker()
    assert test_checker.check("password123") == True

# Returns False if given password has a length of less than 8

def test_returns_error_for_password_length_of_less_than_eight():
    test_checker = PasswordChecker()
    with pytest.raises(Exception) as err:
        test_checker.check("passw")
    error_message = str(err.value)
    assert error_message == "Invalid password, must be 8+ characters."