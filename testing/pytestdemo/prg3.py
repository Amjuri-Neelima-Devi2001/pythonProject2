import pytest
def add(l):
    a=0
    for i in range(len(l)):
        a=l[i]+a
    return a
@pytest.mark.parametrize("l,expected_output",[([10,20,30],60),([1,-1,4],4),([-1.0,2.0,30.0],31.0)])
def test_add(l,expected_output):
    assert add(l)==expected_output
