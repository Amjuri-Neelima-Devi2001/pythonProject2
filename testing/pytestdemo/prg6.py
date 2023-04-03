import pytest
@pytest.fixture
def input_value():
    input=39
    return input
def test_divisible_by_3(input_value):
    assert input_value % 3 ==0
def test_divisiblr_by_13(input_value):
    assert input_value % 13==0