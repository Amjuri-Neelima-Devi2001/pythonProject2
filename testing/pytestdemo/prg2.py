import pytest
def fact(n):
    fact=1
    if n==0:
        return "invalid"
    elif n<0:
        return 'invalid'
    elif n>0:
        for i in range(1,n+1):
            fact=fact*i
    return fact
@pytest.mark.parametrize("n,expected_output",[(2,2),(4,24),(0,'invalid'),(-1,'invalid')])
def test_fact(n, expected_output):
    assert fact(n)==expected_output