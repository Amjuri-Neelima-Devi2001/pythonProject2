import pytest
@pytest.mark.hcl
def test_d1():
    assert 10+5==15

def test_d2():
    assert 10-3==7
@pytest.mark.sz
def test_d3():
    assert 4*5==20
