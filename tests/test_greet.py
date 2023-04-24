from lib.greet import *

def test_greet_returns_kate_for_kate():
    result = greet("Kate")
    assert result == "Hello, Kate!"