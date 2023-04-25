from lib.counter import *

"""
Initial count returns zero, when no numbers are added.
"""

def test_initially_returns_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

"""
Returns the correct count, when one number is added.
"""

def test_returns_correct_count_for_one_number():
    counter = Counter()
    counter.add(15)
    assert counter.report() == "Counted to 15 so far."

"""
Returns the correct count, when multiple numbers are added.
"""

def test_returns_correct_count_for_multiple_numbers():
    counter = Counter()
    counter.add(7)
    counter.add(12)
    counter.add(9)
    assert counter.report() == "Counted to 28 so far."