from lib.gratitudes import *

# Initially returns zero gratitudes, if no gratitudes added.

def test_initially_returns_zero_gratitudes():
    test_gratitudes = Gratitudes()
    assert test_gratitudes.format() == "Be grateful for: "

# Returns one gratitude, when one gratitude is added.

def test_returns_one_gratitude():
    test_gratitudes = Gratitudes()
    test_gratitudes.add("snacks")
    assert test_gratitudes.format() == "Be grateful for: snacks"

# Returns multiple gratitudes in the correct format, 
# when multiple gratitudes are added.

def test_returns_multiple_gratitudes():
    test_gratitudes = Gratitudes()
    test_gratitudes.add("snacks")
    test_gratitudes.add("nice views")
    test_gratitudes.add("support")
    assert test_gratitudes.format() == "Be grateful for: snacks, nice views, support"