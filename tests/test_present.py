import pytest
from lib.present import *

# Returns unwrapped item, when the item has been wrapped

def test_returns_unwrapped_item():
    test_present = Present()
    test_present.wrap("perfume")
    assert test_present.unwrap() == "perfume"

# Returns an error if we try to wrap a second item

def test_returns_error_if_second_item_wrapped():
    test_present = Present()
    test_present.wrap("wrist watch")
    with pytest.raises(Exception) as err:
        test_present.wrap("perfume")
    error_message = str(err.value)
    assert error_message == "A contents has already been wrapped."

# Returns an error if no items have been wrapped

def test_returns_error_if_no_items_wrapped():
    test_present = Present()
    with pytest.raises(Exception) as err:
        test_present.unwrap()
    error_message = str(err.value)
    assert error_message == "No contents have been wrapped."

# The value of the first wrapped item is preserved, when we try to wrap a second item

def test_value_of_first_wrapped_item_is_preserved():
    test_present = Present()
    test_present.wrap("wrist watch")
    with pytest.raises(Exception) as err:
        test_present.wrap("perfume")
    assert test_present.unwrap() == "wrist watch"