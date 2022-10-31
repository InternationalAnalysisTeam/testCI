import double
import pytest

@pytest.mark.parametrize("test_input, expected_output",
                         [(2,4),(-3,-6),(3,6)])
def test_double(test_input, expected_output):
    assert double.double(test_input)==expected_output