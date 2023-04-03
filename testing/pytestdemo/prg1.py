import pytest
def add(a,b):
    return a+b
@pytest.mark.parametrize("a,b,expected_output",[(1,2,3),(10,10,20),(1,-1,0),(0,0,0)])
def test_add(a,b,expected_output):
    assert add(a,b)==expected_output
